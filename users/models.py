from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Exercise(models.Model):
    title = models.CharField(max_length=255)
    photos = models.JSONField()
    seconds_time = models.IntegerField()
    count_calories = models.IntegerField()

    def __str__(self):
        return self.title


class ExerciseUser(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField()
