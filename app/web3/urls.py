from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers

from users.views import UserViewSet, ExerciseViewSet, ExerciseListUserView, ExerciseNotDoingUserView, ExerciseUserViewSet
from web3 import settings
router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'exercise', ExerciseViewSet, basename='exercise')
router.register(r'exercise-user', ExerciseUserViewSet, basename='exercise_user')

users = [
    path('', include(router.urls)),
    path('<str:apiuser>/days', ExerciseListUserView.as_view()),
    path('<str:apiuser>/days/list', ExerciseNotDoingUserView.as_view()),
]

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('admin/', admin.site.urls),
    path('api/', include(users)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

