from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import UserViewSet, ExerciseViewSet, ExerciseUserView
from web3 import settings
router = routers.DefaultRouter()
router.register(r'user/', UserViewSet, basename='user')
router.register(r'exercise/', ExerciseViewSet, basename='exercise')

users = [
    path('<str:apiuser>/days', ExerciseUserView.as_view()),
    path('', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

