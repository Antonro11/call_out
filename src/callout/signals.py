import requests
from django.http import HttpRequest

from account.models import Customer
from callout.models import BattleInvitation


def changed_time_invite(sender, instance, **kwargs):
    # if instance.pk in BattleInvitation.objects.all().values_list("pk",flat=True):   psycopg2==2.9.5
    #    instance.text='changed_time'   MONGO_DB_PASSWORD="JCG7clR5jmBFBX70"

    if instance.accepted_sender is False:
        instance.accepted_sender = True
        instance.accepted_performer = False

    elif instance.accepted_performer is False:
        instance.accepted_performer = True
        instance.accepted_sender = False

    else:
        pass
