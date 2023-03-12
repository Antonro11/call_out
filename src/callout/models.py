import datetime
import random

from django.db import models

from account.models import Customer


class BattleInvitation(models.Model):
    performer = models.ForeignKey(Customer, related_name="performer", on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(Customer, related_name="sender", on_delete=models.CASCADE, null=True)
    date_and_time = models.DateTimeField(default=datetime.datetime.now())
    music_style = models.CharField(
        choices=(("Popping", "Popping"), ("Hip-hop", "Hip-hop"), ("Experimental", "Experimental")),  # NOQA
        max_length=50,
        null=True,
    )
    text = models.CharField(max_length=120, null=True)
    accepted_sender = models.BooleanField(default=False)
    accepted_performer = models.BooleanField(default=False)

    @classmethod
    def generate_invitation(cls, count):
        battle_pk_lst = Battle.objects.all().values_list("pk", flat=True)
        performer_pk_lst = Customer.objects.all().values_list("pk", flat=True)
        for i in range(count):
            cls.objects.create(
                battle=Battle.objects.get(pk=random.choice(battle_pk_lst)),
                performer=Customer.objects.get(pk=random.choice(performer_pk_lst)),
                date_and_time=datetime.datetime.now(),
                music_style=random.choice(["Popping", "Hip-hop", "Experimental"]),
                accepted=random.choice([True, False]),
            )

    def __str__(self):
        return f"{self.sender.nickname} invited {self.performer.nickname} ({self.date_and_time})"


class Battle(models.Model):
    who_made_callout = models.ForeignKey(
        Customer, related_name="who_made_callout", on_delete=models.CASCADE, default=False
    )
    who_accepted_callout = models.ForeignKey(
        Customer, related_name="who_accepted_callout", on_delete=models.CASCADE, default=False
    )
    start_time = models.DateTimeField(default=datetime.datetime.now())
    rounds_count = models.PositiveIntegerField(default=2)
    music = models.CharField(max_length=255)
    result_score = models.PositiveIntegerField(default=0)
    invitation = models.ForeignKey(BattleInvitation, on_delete=models.CASCADE, null=True)

    @classmethod
    def generate_battles(cls, count):
        customers_pk_lst = Customer.objects.all().values_list("pk", flat=True)
        for i in range(count):
            cls.objects.create(
                start_time=datetime.datetime.now(),
                rounds_count=random.choice([2, 3]),
                music=f"url/track{str(random.randint(1,50))}.mp3",
                result_score=random.choice([0, 50]),
                result_goes_to=Customer.objects.get(pk=random.choice(customers_pk_lst)),
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
