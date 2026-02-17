from rest_framework import serializers
from .models import FoodRequest
from django.contrib.auth import get_user_model
from donations.serializers import DonationSerializer

User = get_user_model()


class ReceiverMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "organization_name"]


class FoodRequestSerializer(serializers.ModelSerializer):
    receiver = ReceiverMiniSerializer(read_only=True)
    donation = DonationSerializer(read_only=True)

    class Meta:
        model = FoodRequest
        fields = [
            'id',
            'receiver',
            'receiver_location',
            'donation',
            'status',
            'requested_at',
        ]
