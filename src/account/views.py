import os
import random

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from account.models import Customer
from callout.models import Battle, BattleInvitation
from config.settings.base import BASE_DIR


# Create your views here.
class PerformerProfile(DetailView):
    template_name = "users/performer_profile.html"
    model = get_user_model()


class SpectatorProfile(DetailView):
    template_name = "users/spectator_profile.html"
    model = get_user_model()


class UpdateInvite(UpdateView):
    model = BattleInvitation
    fields = ["date_and_time"]
    template_name = "users/change_time.html"
    success_url = reverse_lazy("core:index")


class Invites(ListView):
    template_name = "users/invites.html"
    model = get_user_model()

    def post(self, request, *args, **kwargs):
        instance_user = Customer.objects.get(pk=self.request.user.pk)

        if "canсel_invitation" in self.request.POST:
            battle_instance = BattleInvitation.objects.get(pk=self.request.POST.get("canсel_invitation"))
            battle_instance.sender.invitations.remove(battle_instance)
            instance_user.invitations.remove(battle_instance)
            BattleInvitation.objects.filter(pk=battle_instance.pk).delete()
        elif "change_time" in self.request.POST:
            battle_instance = BattleInvitation.objects.get(pk=self.request.POST.get("change_time"))

            return HttpResponseRedirect(reverse_lazy("account:change_time", kwargs={"pk": battle_instance.pk}))
        elif "accept_invitation" in self.request.POST:
            battle_invitation_instance = BattleInvitation.objects.get(pk=self.request.POST.get("accept_invitation"))
            battle_instance = Battle.objects.create(
                who_made_callout=battle_invitation_instance.sender,
                who_accepted_callout=battle_invitation_instance.performer,
                start_time=battle_invitation_instance.date_and_time,
                rounds_count=random.choice([2, 3]),
                music=battle_invitation_instance.music_style,
            )
            battle_instance.save()
            tracks = [i for i in os.listdir(str(BASE_DIR) + "/static/music/" + battle_instance.music + "/")]

            track_one = random.choice(tracks)
            tracks.remove(track_one)
            battle_instance.track_one = track_one

            track_two = random.choice(tracks)
            tracks.remove(track_two)
            battle_instance.track_two = track_two

            track_three = random.choice(tracks)
            tracks.remove(track_three)
            battle_instance.track_three = track_three
            battle_instance.save()
            print(tracks)

            sender = Customer.objects.get(pk=battle_instance.who_made_callout.pk)
            performer = Customer.objects.get(pk=battle_instance.who_accepted_callout.pk)
            sender.battles.add(battle_instance)
            performer.battles.add(battle_instance)
            sender.invitations.remove(battle_invitation_instance)
            performer.invitations.remove(battle_invitation_instance)

            return HttpResponseRedirect(
                reverse_lazy("callout:battle-room", kwargs={"pk": battle_invitation_instance.pk})
            )

        return HttpResponseRedirect(reverse_lazy("account:invites", kwargs={"pk": instance_user.pk}))


class Battles(ListView):
    template_name = "users/battles.html"
    model = get_user_model()
