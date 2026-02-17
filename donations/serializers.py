from rest_framework import serializers
from .models import Donation
from requests.models import FoodRequest


class DonationSerializer(serializers.ModelSerializer):
    has_requested = serializers.SerializerMethodField()

    class Meta:
        model = Donation
        fields = [
            'id',
            'food_name',
            'food_category',
            'food_type',
            'quantity',
            'expiry_time',
            'pickup_address',
            'notes',
            'status',
            'created_at',
            'has_requested',   
        ]
        read_only_fields = ('status', 'created_at')

    def get_has_requested(self, obj):
        request = self.context.get("request")

        if not request or not request.user.is_authenticated:
            return False

        return FoodRequest.objects.filter(
            donation=obj,
            receiver=request.user
        ).exists()
