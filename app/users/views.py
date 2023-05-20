from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.models import Exercise
from users.serializer import UserSerializer, ExerciseSerializer


# Create your views here.
@extend_schema(
    tags=['User']
)
class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExerciseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer