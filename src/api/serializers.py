from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from account.models import Customer
from callout.models import Battle, BattleInvitation, BattleVote


class SubscriptionsSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("nickname", "dance_style", "pk")


class CustomerSerializer(ModelSerializer):
    subscribtions = SubscriptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "subscribtions", "pk")


class BattleSerializer(ModelSerializer):
    class Meta:
        model = Battle
        fields = ("music", "rounds_count", "pk")


class BattleInvitationSerializer(ModelSerializer):
    performer = SubscriptionsSerializer(read_only=True)
    battle = BattleSerializer(read_only=True)

    class Meta:
        model = BattleInvitation
        fields = ("battle", "performer", "pk")


class BattleVoteSerializer(ModelSerializer):
    battle = BattleSerializer(read_only=True)
    voter = SubscriptionsSerializer(read_only=True)

    class Meta:
        model = BattleVote
        fields = ("battle", "voter", "pk")
