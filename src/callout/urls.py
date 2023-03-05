from django.urls import path

from callout.views import Invitation

app_name = "callout"

urlpatterns = [
    path("invite/<int:pk>/", Invitation.as_view(), name="invite"),
]
