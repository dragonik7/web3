from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Exercise, ExerciseUser
from users.serializer import ExerciseSerializer, ExerciseUserSerializer, ApiUsersSerializer


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


class ExerciseUserView(APIView):
    serializer_class = ExerciseUserSerializer

    def get(self, request, apiuser):
        queryset = ExerciseUser.objects.values('date').annotate(Sum('points')).filter(user_id=apiuser)
        print(queryset.query)
        return Response(list(queryset))
