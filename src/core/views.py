from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from account.forms import PerformerRegistrationForm, SpectatorRegistrationForm
from account.models import Customer


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class CustomerLogin(LoginView):
    template_name = "registration/login.html"
    next_page = reverse_lazy("core:index")


class CustomerLogout(LogoutView):
    next_page = reverse_lazy("core:index")


class PerformerRegistration(CreateView):
    template_name = "registration/performer_registration.html"
    form_class = PerformerRegistrationForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_type = "performer"
        user = form.save()

        login(self.request, user=user, backend="django.contrib.auth.backends.ModelBackend")
        return HttpResponseRedirect(reverse_lazy("core:index"))


class SpectatorRegistration(CreateView):
    template_name = "registration/spectator-registration.html"
    form_class = SpectatorRegistrationForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_type = "spectator"
        user = form.save()

        login(self.request, user=user, backend="django.contrib.auth.backends.ModelBackend")
        return HttpResponseRedirect(reverse_lazy("core:index"))


class PerformerList(ListView):
    template_name = "users/list_performers.html"
    model = Customer

    def get(self, request, *args, **kwargs):
        all_users = self.request.user.subscribtions.values()
        self.extra_context = {"all_users": [i["email"] for i in all_users]}
        return super(PerformerList, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        instance_user = Customer.objects.get(pk=self.request.user.pk)

        if "performer_pk" in self.request.POST:
            instance_subscription = Customer.objects.get(pk=self.request.POST.get("performer_pk"))
            instance_user.subscribtions.add(instance_subscription)
        elif "performer_unsubscribe" in self.request.POST:
            instance_subscription = Customer.objects.get(pk=self.request.POST.get("performer_unsubscribe"))
            instance_user.subscribtions.remove(instance_subscription)
        elif "callout" in self.request.POST:
            instance_callout = Customer.objects.get(pk=self.request.POST.get("callout"))
            self.request.session["performer_pk"] = instance_callout.pk
            return HttpResponseRedirect(reverse_lazy("callout:invite", kwargs={"pk": instance_callout.pk}))
        print(
            instance_subscription, instance_user, instance_user.subscribtions.all()
        )  # self.request.POST["performer_pk"])
        return HttpResponseRedirect(reverse_lazy("core:list-performers"))
