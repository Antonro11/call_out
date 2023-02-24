from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from account.models import Customer
from api.serializers import (BattleInvitationSerializer, BattleSerializer,
                             BattleVoteSerializer, CustomerSerializer)
from callout.models import Battle, BattleInvitation, BattleVote


class CustomerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class BattleViewSet(ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class BattleInvitationViewSet(ModelViewSet):
    queryset = BattleInvitation.objects.all()
    serializer_class = BattleInvitationSerializer


class BattleVoteViewSet(ModelViewSet):
    queryset = BattleVote.objects.all()
    serializer_class = BattleVoteSerializer


class CustomerGetSet(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDeleteView(DestroyAPIView):
    queryset = Customer.objects.all()


class CustomerUpdateView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ["patch"]


class BattleCreateView(CreateAPIView):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class BattleDeleteView(DestroyAPIView):
    queryset = Battle.objects.all()


class BattleUpdateView(UpdateAPIView):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
    http_method_names = ["patch"]


class BattleInvitationCreateView(CreateAPIView):
    queryset = BattleInvitation.objects.all()
    serializer_class = BattleInvitationSerializer


class BattleInvitationDeleteView(DestroyAPIView):
    queryset = BattleInvitation.objects.all()


class BattleInvitationUpdateView(UpdateAPIView):
    queryset = BattleInvitation.objects.all()
    serializer_class = BattleInvitationSerializer
    http_method_names = ["patch"]


class BattleVoteCreateView(CreateAPIView):
    queryset = BattleVote.objects.all()
    serializer_class = BattleVoteSerializer


class BattleVoteDeleteView(DestroyAPIView):
    queryset = BattleVote.objects.all()


class BattleVoteUpdateView(UpdateAPIView):
    queryset = BattleVote.objects.all()
    serializer_class = BattleVoteSerializer
    http_method_names = ["patch"]
