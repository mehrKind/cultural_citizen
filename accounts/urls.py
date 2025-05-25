from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  SignupView, UserProfileDetailApiView, UserProfileView, LoginView
from .import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profiles/', views.UserProfileView.as_view() ),
    path('profiles/<int:profile_id>', views.UserProfileDetailApiView.as_view()),
]
