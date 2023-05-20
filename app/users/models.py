from django.db import models


class ApiUser(models.Model):
    id = models.CharField(max_length=200, unique=True, primary_key=True)
    first_name = models.CharField(max_length=200)


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    photos = models.JSONField()
    seconds_time = models.IntegerField()
    count_calories = models.IntegerField()
    point = models.IntegerField()
    users = models.ManyToManyField(ApiUser, through="ExerciseUser")

    def __str__(self):
        return self.title


class ExerciseUser(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    points = models.IntegerField(default=10)
