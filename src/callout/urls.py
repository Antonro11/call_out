from django.urls import path, re_path

from callout.views import BattleRoom, Invitation

app_name = "callout"

urlpatterns = [
    path("invite/<int:pk>/", Invitation.as_view(), name="invite"),
    path("battle-room/<int:pk>/,", BattleRoom.as_view(), name="battle-room"),
]
