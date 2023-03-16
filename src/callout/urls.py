from django.urls import path

from callout.views import BattleRoom, Invitation, video_feed

app_name = "callout"

urlpatterns = [
    path("invite/<int:pk>/", Invitation.as_view(), name="invite"),
    path("battle-room/<int:pk>/", BattleRoom.as_view(), name="battle-room"),
    path("video/", video_feed, name="video"),
]
