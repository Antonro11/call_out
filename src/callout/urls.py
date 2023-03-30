from django.urls import path

from callout.views import BattleRoom, BattleRoomRemote, Invitation, video_feed

app_name = "callout"

urlpatterns = [
    path("invite/<int:pk>/", Invitation.as_view(), name="invite"),
    path("battle-room/<int:pk>/", BattleRoom.as_view(), name="battle-room"),
    path("battle-room/consumer/<int:pk>/", BattleRoomRemote.as_view(), name="battle-room-remote"),
    path("video/", video_feed, name="video"),
]
