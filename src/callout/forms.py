from django.forms import ModelForm

from callout.models import BattleInvitation


class BattleInvitationForm(ModelForm):
    class Meta:
        model = BattleInvitation
        fields = ("date_and_time", "music_style")
