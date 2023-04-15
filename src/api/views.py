from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from account.models import Customer
from api.serializers import (BattleInvitationSerializer, BattleSerializer,
                             BattleVoteSerializer, CustomerSerializer)
from callout.models import Battle, BattleInvitation, BattleVote
from core.permissions import AuthenticatedAdmin, AuthenticatedNotAdmin


class CustomerViewSet(ModelViewSet):
    permission_classes = [AuthenticatedNotAdmin | AuthenticatedAdmin]
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class BattleViewSet(ModelViewSet):
    permission_classes = [AuthenticatedNotAdmin | AuthenticatedAdmin]
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class BattleInvitationViewSet(ModelViewSet):
    permission_classes = [AuthenticatedNotAdmin | AuthenticatedAdmin]
    queryset = BattleInvitation.objects.all()
    serializer_class = BattleInvitationSerializer


class BattleVoteViewSet(ModelViewSet):
    permission_classes = [AuthenticatedNotAdmin | AuthenticatedAdmin]
    queryset = BattleVote.objects.all()
    serializer_class = BattleVoteSerializer


class CustomerGetSet(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedNotAdmin | AuthenticatedAdmin]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCreateView(CreateAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ["patch"]


class BattleCreateView(CreateAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class BattleDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class BattleUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
    http_method_names = ["patch"]


class BattleInvitationCreateView(CreateAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = BattleInvitation.objects.all()
    serializer_class = BattleInvitationSerializer


class BattleInvitationDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = BattleInvitation.objects.all()
    serializer_class = BattleInvitationSerializer


class BattleInvitationUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = BattleInvitation.objects.all()
    serializer_class = BattleInvitationSerializer
    http_method_names = ["patch"]


class BattleVoteCreateView(CreateAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = BattleVote.objects.all()
    serializer_class = BattleVoteSerializer


class BattleVoteDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = BattleVote.objects.all()


class BattleVoteUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthenticatedAdmin]
    queryset = BattleVote.objects.all()
    serializer_class = BattleVoteSerializer
    http_method_names = ["patch"]
