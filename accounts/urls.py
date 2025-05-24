from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  SignupView, UserProfileDetailApiView, UserProfileView
from .import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profiles/', views.UserProfileView.as_view() ),
    path('profiles/<int:profile_id>', views.UserProfileDetailApiView.as_view()),
]
