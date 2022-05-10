from django.urls import include, path
from .views import  ForgotAPIView, LoginAPIView, LogoutView, RegisterAPIView, ResetAPIView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register',RegisterAPIView.as_view()),
    path('login',LoginAPIView.as_view()),
    path('logout',LogoutView.as_view()),
    path('user',UserView.as_view()),
    path('forgot',ForgotAPIView.as_view()),
    path('reset',ResetAPIView.as_view()),
]
