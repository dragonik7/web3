from rest_framework import serializers

from users.models import Exercise, ExerciseUser, ApiUser


class ApiUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('id', 'first_name')

    def create(self, validated_data):
        return ApiUser.objects.create(
            id=validated_data['id'],
            first_name=validated_data['first_name']
        )


class ExerciseSerializer(serializers.ModelSerializer):
    photos = serializers.JSONField()

    class Meta:
        model = Exercise
        fields = ('title', 'photos', 'seconds_time', 'count_calories', 'point')


class ExerciseUserSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer

    class Meta:
        model = ExerciseUser
        fields = ('date', 'exercise')


class ExerciseNotDoingSerializer(serializers.ModelSerializer):
    exercise = ExerciseUserSerializer

    class Meta:
        model = Exercise
        fields = '__all__'


class ExerciseUserCreateSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer
    class Meta:
        model = ExerciseUser
        fields = ('user', 'exercise')

    def create(self, validated_data):
        return ExerciseUser.objects.create(
            user=validated_data['user'],
            exercise=validated_data['exercise']
        )