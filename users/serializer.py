from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Exercise


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username')

    def create(self, validated_data):
        return User.objects.create(
            username=validated_data['username'],
        )


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('title', 'photos', 'seconds_time', 'count_calories')
