from django.urls import path

from core.views import IndexView, PerformerList, TestTwoIndexView

app_name = "core"

urlpatterns = [
    path("", TestTwoIndexView.as_view(), name="index"),
    path("list-performers", PerformerList.as_view(), name="list-performers"),
    path("old-index/", IndexView.as_view(), name="old-index"),
]
