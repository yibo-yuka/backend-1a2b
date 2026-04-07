from rest_framework import serializers
from .models import UserScore

class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ['id', 'username', 'score', 'created_at']