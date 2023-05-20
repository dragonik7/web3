from django.contrib import admin

from users.models import Exercise, ExerciseUser, ApiUser


@admin.register(ApiUser)
class ApiUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'photos', 'seconds_time', 'count_calories')


@admin.register(ExerciseUser)
class ExerciseUserAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'user', 'date')
