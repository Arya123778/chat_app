from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import RegisterView, LogoutView, ProfileView, ChangePasswordView
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('change-password/',ChangePasswordView.as_view())
]
