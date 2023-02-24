from django.urls import path

from core.views import IndexView, PerformerList

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("list-performers", PerformerList.as_view(), name="list-performers"),
]
