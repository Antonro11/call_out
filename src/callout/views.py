from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from account.models import Customer
from callout.forms import BattleInvitationForm
from callout.models import Battle, BattleInvitation


class Invitation(CreateView):
    model = BattleInvitation
    form_class = BattleInvitationForm
    template_name = "callout/invitation.html"

    def get_context_data(self, **kwargs):
        self.extra_context = {"performer_pk": self.request.session["performer_pk"]}
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.performer = Customer.objects.get(pk=self.request.session["performer_pk"])
        self.object.sender = Customer.objects.get(pk=self.request.user.pk)
        self.object.save()
        instance_user = Customer.objects.get(pk=self.request.user.pk)
        instance_performer = Customer.objects.get(pk=self.request.session["performer_pk"])
        instance_performer.invitations.add(self.object)
        instance_user.invitations.add(self.object)

        return HttpResponseRedirect(reverse_lazy("core:index"))
