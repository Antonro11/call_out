from django.urls import path

from account.views import (Invites, PerformerProfile, SpectatorProfile,
                           UpdateInvite)
from core.views import (CustomerLogin, CustomerLogout, PerformerRegistration,
                        SpectatorRegistration)

app_name = "account"

urlpatterns = [
    path("performer-registration/", PerformerRegistration.as_view(), name="performer-registration"),
    path("spectator-registration/", SpectatorRegistration.as_view(), name="spectator-registration"),
    path("login/", CustomerLogin.as_view(), name="login"),
    path("logout/", CustomerLogout.as_view(), name="logout"),
    path("performer-profile/<int:pk>/", PerformerProfile.as_view(), name="performer-profile"),
    path("spectator-profile/<int:pk>/", SpectatorProfile.as_view(), name="spectator-profile"),
    path("invites/<int:pk>/", Invites.as_view(), name="invites"),
    path("change_time/<int:pk>/", UpdateInvite.as_view(), name="change_time"),
]
