import datetime
import random

from django.db import models

from account.models import Customer


class BattleInvitation(models.Model):
    performer = models.ForeignKey(
        Customer, related_name="performer", on_delete=models.CASCADE, blank=True, default=None
    )
    sender = models.ForeignKey(Customer, related_name="sender", on_delete=models.CASCADE, blank=True, default=None)
    date_and_time = models.DateTimeField(default=datetime.datetime.now())
    music_style = models.CharField(
        choices=(("Popping", "Popping"), ("Hip-hop", "Hip-hop"), ("Experimental", "Experimental")),  # NOQA
        max_length=50,
        null=True,
    )
    text = models.CharField(max_length=120, null=True)
    accepted_sender = models.BooleanField(default=False)
    accepted_performer = models.BooleanField(default=False)

    def generate_invitations(count):
        performer_pk_lst = [i for i in Customer.objects.filter(user_type="performer").values_list("pk", flat=True)]
        all_invitations_sender = [i["sender_id"] for i in BattleInvitation.objects.values()]
        all_invitations_performer = [i["performer_id"] for i in BattleInvitation.objects.values()]
        for i in range(count):
            if len(performer_pk_lst) <= 2:
                raise "You should generate more performers"
            performer = random.choice(performer_pk_lst)
            performer_pk_lst.remove(performer)
            sender = random.choice(performer_pk_lst)

            if ((performer in all_invitations_sender) or (performer in all_invitations_performer)) and (
                (sender in all_invitations_sender) or (sender in all_invitations_performer)
            ):  # NOQA
                continue
            instance = BattleInvitation.objects.create(
                date_and_time=datetime.datetime.now(),
                performer=Customer.objects.get(pk=performer),
                sender=Customer.objects.get(pk=sender),
                music_style=random.choice(["Popping", "Hip-hop", "Experimental"]),
            )
            Customer.objects.get(pk=instance.sender.pk).invitations.add(instance)
            Customer.objects.get(pk=instance.performer.pk).invitations.add(instance)

    def __str__(self):
        return f"{self.sender.nickname} invited {self.performer.nickname} ({self.date_and_time})"


class Battle(models.Model):
    who_made_callout = models.ForeignKey(
        Customer, related_name="who_made_callout", on_delete=models.CASCADE, null=True
    )
    who_accepted_callout = models.ForeignKey(
        Customer, related_name="who_accepted_callout", on_delete=models.CASCADE, null=True
    )
    start_time = models.DateTimeField(default=datetime.datetime.now())
    rounds_count = models.PositiveIntegerField(default=2)
    music = models.CharField(max_length=255)
    result_score = models.PositiveIntegerField(default=0)
    invitation = models.ForeignKey(BattleInvitation, on_delete=models.CASCADE, null=True)
    track_one = models.CharField(max_length=255, null=True)
    track_two = models.CharField(max_length=255, null=True)
    track_three = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.who_made_callout.nickname} VS {self.who_accepted_callout.nickname} ({self.start_time})"

    @classmethod
    def generate_battles(cls, count):
        for i in range(count):
            cls.objects.create(
                start_time=datetime.datetime.now(),
                rounds_count=random.choice([2, 3]),
                music=f"url/track{str(random.randint(1,50))}.mp3",
                result_score=random.choice([0, 50]),
            )


class BattleVote(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)
    performer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    voter = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="votes")
    vote_timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def generate_vote(cls, count):
        battle_pk_lst = Battle.objects.all().values_list("pk", flat=True)
        voter_pk_lst = Customer.objects.all().values_list("pk", flat=True)
        for i in range(count):
            cls.objects.create(
                battle=Battle.objects.get(pk=random.choice(battle_pk_lst)),
                performer=Customer.objects.get(pk=random.choice(voter_pk_lst)),
                voter=Customer.objects.get(pk=random.choice(voter_pk_lst)),
                vote_timestamp=datetime.datetime.now(),
            )
