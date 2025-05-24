from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import UserProfile , User
from .serializers import UserProfileSerializer, SignupSerializer
from rest_framework import status 
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class UserProfileView(APIView):
    permission_classes = [AllowAny]
    def get(self, request: Request):
        profiles = UserProfile.objects.order_by('id').all()
        ProfileSerializer = UserProfileSerializer(profiles, many=True)
        return Response({
                "status": 200,
                "date": ProfileSerializer.data,
                "error": None
            }, status=status.HTTP_200_OK)
    

    def post(self, request: Request):
        
        creatprofileserializer = UserProfileSerializer(data = request.data)
        if creatprofileserializer.is_valid(): 
            creatprofileserializer.save()
            return Response({
                "status": 200,
                "date":creatprofileserializer.data,
                "error": None
            }, status=status.HTTP_200_OK)
        else:
            return Response({
            "status": 400,
            "data": None,
            "error": creatprofileserializer.errors
        }, status= status.HTTP_400_BAD_REQUEST)

class UserProfileDetailApiView(APIView):
    permission_classes = [AllowAny]
    def get_object(self, profile_id:int):
        try:
            profile = UserProfile.objects.get(pk=profile_id)
            return profile
        
        except UserProfile.DoesNotExist:
            return Response({
            "status": 400,
            "data": None,
            "error": None
        }, status= status.HTTP_400_BAD_REQUEST)
        

    def get(self, request: Request, profile_id:int):
        profile = self.get_object(profile_id)
        serializer = UserProfileSerializer(profile)
        return Response({
                "status": 200,
                "date":serializer.data,
                "error": None
            }, status=status.HTTP_200_OK)
    

    def put(self, request: Request, profile_id:int):
        profile = self.get_object(profile_id)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "date":serializer.data,
                "error": None
            }, status=status.HTTP_200_OK)
        
        return Response({
            "status": 400,
            "data": None,
            "error": serializer.errors
        }, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, profile_id:int):
        profile = self.get_object(profile_id)
        profile.delete()
        return Response({
                "status": 200,
                "date":None,
                "error": None
            }, status=status.HTTP_200_OK)



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
