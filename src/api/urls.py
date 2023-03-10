from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (BattleCreateView, BattleDeleteView,
                       BattleInvitationCreateView, BattleInvitationDeleteView,
                       BattleInvitationUpdateView, BattleInvitationViewSet,
                       BattleUpdateView, BattleViewSet, BattleVoteCreateView,
                       BattleVoteDeleteView, BattleVoteUpdateView,
                       BattleVoteViewSet, CustomerCreateView,
                       CustomerDeleteView, CustomerGetSet, CustomerUpdateView,
                       CustomerViewSet)

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)
router.register("battles", BattleViewSet, "battles")
router.register("battle-invitation", BattleInvitationViewSet)
router.register("battle-vote", BattleVoteViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Call_Out API",
        default_version="v1",
        description="API for making battle",
        terms_of_service="https://policies.google.com/terms",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", include(router.urls)),
    path("create-customer/", CustomerCreateView.as_view(), name="create-customer"),
    path("delete-customer/<int:pk>", CustomerDeleteView.as_view(), name="delete-customer"),
    path("update-customer/<int:pk>", CustomerUpdateView.as_view(), name="update-customer"),
    path("get-customer/<int:pk>", CustomerGetSet.as_view(), name="get-customer"),
    path("create-battle/", BattleCreateView.as_view(), name="create-battle"),
    path("delete-battle/<int:pk>", BattleDeleteView.as_view(), name="delete-battle"),
    path("update-battle/<int:pk>", BattleUpdateView.as_view(), name="update-battle"),
    path("create-battle-invitation/", BattleInvitationCreateView.as_view(), name="create-battle-invitation"),
    path("delete-battle-invitation/<int:pk>", BattleInvitationDeleteView.as_view(), name="delete-battle-invitation"),
    path("update-battle-invitation/<int:pk>", BattleInvitationUpdateView.as_view(), name="update-battle-invitation"),
    path("create-battle-vote/", BattleVoteCreateView.as_view(), name="create-battle-vote"),
    path("delete-battle-vote/<int:pk>", BattleVoteDeleteView.as_view(), name="delete-battle-vote"),
    path("update-battle-vote/<int:pk>", BattleVoteUpdateView.as_view(), name="update-battle-vote"),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("redoc"), name="swagger-docs"),
]
