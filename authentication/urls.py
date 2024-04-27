from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import RegisterUserView, CustomTokenObtainPairView


urlpatterns = [
    path('authentication/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/', TokenRefreshView.as_view(), name='token_verify'),
    path('authentication/register/', RegisterUserView.as_view(), name='register'),
]
