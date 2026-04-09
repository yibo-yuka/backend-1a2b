from rest_framework import serializers
from .models import UserScore

class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ['id', 'username', 'score', 'created_at']
    def validate_username(self, value):
        """
        因為我們要在同一個 Endpoint 處理『更新』邏輯，
        所以要在 Serializer 層級放寬唯一性檢查，改由 View 處理。
        """
        return value