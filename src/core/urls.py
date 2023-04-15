from django.urls import path

import core.views
from core.views import IndexView, PerformerList

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("list-performers/", PerformerList.as_view(), name="list-performers"),
    path("generating-performers/<int:count>/", core.views.generating_performers, name="generating-performers"),
    path("generating-invitations/<int:count>/", core.views.generating_invitations, name="generating-invitations"),
    path("generating-battles/<int:count>/", core.views.generating_battles, name="generating-battles"),
]
