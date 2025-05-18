from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import UserProfile , User
from .serializers import UserProfileSerializer, UserSerializer , SignupSerializer
from rest_framework import status , viewsets, mixins, generics
from rest_framework.permissions import AllowAny


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SignupView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.order_by('id')
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            UserProfile.objects.create(user=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)