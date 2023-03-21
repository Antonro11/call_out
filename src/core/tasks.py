import datetime
import random
import time

from celery import shared_task
from django.http import JsonResponse
from faker import Faker

from account.models import Customer
from callout.models import Battle, BattleInvitation
from config.celery import app


@shared_task
def task_test():
    print("AAAAA")


@shared_task
def generate_performers(count):
    faker = Faker()
    for i in range(count):
        Customer.objects.create(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            nickname=faker.first_name()[:2] + faker.last_name()[:2],
            gender=random.choice(["M", "F"]),
            dance_style=random.choice(["Popping", "Hip-hop", "Experimental"]),
            password="example",
            user_type="performer",
        )


@shared_task
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


@shared_task
def generate_battles(count):
    for i in range(count):
        Battle.objects.create(
            start_time=datetime.datetime.now(),
            rounds_count=random.choice([2, 3]),
            music=f"url/track{str(random.randint(1,50))}.mp3",
            result_score=random.choice([0, 50]),
        )
