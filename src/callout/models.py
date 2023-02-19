import datetime

from django.db import models

from account.models import Customer


class Battle(models.Model):
    start_time = models.DateTimeField(default=datetime.datetime.now())
    rounds_count = models.PositiveIntegerField(default=2)
    music = models.CharField(max_length=255)
    result_score = models.PositiveIntegerField(default=0)
    result_goes_to = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


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


class BattleVote(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)
    performer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    voter = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="votes")
    vote_timestamp = models.DateTimeField(auto_now_add=True)
