from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView


# Create your views here.
class PerformerProfile(DetailView):
    template_name = "users/performer_profile.html"
    model = get_user_model()


class SpectatorProfile(DetailView):
    template_name = "users/spectator_profile.html"
    model = get_user_model()
