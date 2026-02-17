from rest_framework import serializers
from .models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "organization_name", "role"]
        read_only_fields = ["email", "role"]
