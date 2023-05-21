from django.db.models.aggregates import Sum
from django.db.models.functions import TruncMonth, TruncDate
from django.db.models.query_utils import Q
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Exercise, ExerciseUser, ApiUser
from users.serializer import ExerciseSerializer, ExerciseUserSerializer, ApiUsersSerializer, ExerciseNotDoingSerializer, \
    ExerciseUserCreateSerializer


# Create your views here.
@extend_schema(
    tags=['User']
)
class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = ApiUsersSerializer


class ExerciseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseUserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ExerciseUserCreateSerializer

    def get_queryset(self):
        return ExerciseUser.objects.all()


class ExerciseListUserView(APIView):
    serializer_class = ExerciseUserSerializer

    def get(self, request, apiuser):
        queryset = ExerciseUser.objects.annotate(day=TruncDate('date')).values('day').annotate(total_points=Sum('exercise__point')).filter(user_id=apiuser)
        return Response(list(queryset))


class ExerciseNotDoingUserView(APIView):
    serializer_class = ExerciseNotDoingSerializer

    def get(self, request, apiuser):
        queryset = Exercise.objects.raw('select * from users_exercise e left join users_exerciseuser eu on eu.exercise_id = e.id where eu.id is null or user_id not like %s', [apiuser])
        return Response(self.serializer_class(queryset, many=True).data)


class ExerciseMonthCountUserView(APIView):

    def get(self, request, apiuser):
        queryset = ExerciseUser.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_points=Sum('exercise__point')).filter(user_id=apiuser)
        return Response(list(queryset))
