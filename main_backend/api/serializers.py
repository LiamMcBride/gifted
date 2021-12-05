from main_backend.models import User, Event
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "id", "events"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name", "id"]