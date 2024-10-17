from rest_framework import serializers
from .models import CustomUser
from apps.events.serializers import EventSerializer


class UserSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "events", "date_joined"]
