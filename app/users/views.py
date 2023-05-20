from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from django.db.models.query_utils import Q
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Exercise, ExerciseUser
from users.serializer import ExerciseSerializer, ExerciseUserSerializer, ApiUsersSerializer, ExerciseNotDoingSerializer


# Create your views here.
@extend_schema(
    tags=['User']
)
class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ApiUsersSerializer


class ExerciseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseUserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ExerciseUserSerializer

    def get_queryset(self):
        return ExerciseUser.objects.filter(user_id=self.request.user.id).order_by('-data')


class ExerciseListUserView(APIView):
    serializer_class = ExerciseUserSerializer

    def get(self, request, apiuser):
        queryset = Exercise.objects.all().select_related('users_exercise').values('exerciseuser__date').annotate(
            Sum('point')).filter(Q(users__id=apiuser))
        return Response(list(queryset))


class ExerciseNotDoingUserView(APIView):
    serializer_class = ExerciseNotDoingSerializer

    def get(self, request, apiuser):
        queryset = Exercise.objects.raw('select * from users_exercise e left join users_exerciseuser eu on eu.exercise_id = e.id where eu.id is null')
        return Response(self.serializer_class(queryset, many=True).data)
