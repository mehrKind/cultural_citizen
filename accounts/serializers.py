from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Student, Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):

    #Nested serializer
    user = UserSerializer()
    class Meta:
        model = UserProfile 
        fields = '__all__' 
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')  #extract the user  part from the profile data and pop in `user_data`.
        user = User.objects.create(**user_data) #we create an object of the user model From the data we got from user_data 
        profile = UserProfile.objects.create(user=user, **validated_data) 

        return profile
    

    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
