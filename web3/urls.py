from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from users.views import UserViewSet, ExerciseViewSet
from web3 import settings

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'exercise', ExerciseViewSet)


token = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

users = [
    path('auth/', include(token)),
    path('', include(router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

