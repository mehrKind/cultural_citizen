from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import UserProfile , User
from .serializers import UserProfileSerializer, SignupSerializer
from rest_framework import status , viewsets, mixins, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request: Request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": 200,
                "date":{
                    "username": user.username,
                    "email": user.email,
                },
                "error": None
            }, status=status.HTTP_200_OK)
        
        return Response({
            "status": 400,
            "data": None,
            "error": serializer.errors
        }, status= status.HTTP_400_BAD_REQUEST)
