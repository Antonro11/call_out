import datetime
import random

from django.db import models

from account.models import Customer


class Battle(models.Model):
    start_time = models.DateTimeField(default=datetime.datetime.now())
    rounds_count = models.PositiveIntegerField(default=2)
    music = models.CharField(max_length=255)
    result_score = models.PositiveIntegerField(default=0)
    result_goes_to = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

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


class BattleInvitation(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)
    performer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(default=datetime.datetime.now())
    music_style = models.CharField(
        choices=(("Popping", "Popping"), ("Hip-hop", "Hip-hop"), ("Experimental", "Experimental")),  # NOQA
        max_length=50,
        null=True,
    )
    accepted = models.BooleanField(default=False)

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
