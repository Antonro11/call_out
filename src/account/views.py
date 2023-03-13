from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from account.models import Customer
from callout.models import BattleInvitation


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
            battle_instance = BattleInvitation.objects.get(pk=self.request.POST.get("accept_invitation"))
            return HttpResponseRedirect(reverse_lazy("callout:battle-room", kwargs={"pk": battle_instance.pk}))

        return HttpResponseRedirect(reverse_lazy("account:invites", kwargs={"pk": instance_user.pk}))
