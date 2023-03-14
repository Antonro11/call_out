from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save


class CalloutConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "callout"

    def ready(
        self,
    ):
        from callout.models import BattleInvitation
        from callout.signals import changed_time_invite

        pre_save.connect(changed_time_invite, BattleInvitation)
