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

    # Defining additional fields.
    
    full_name = serializers.CharField(write_only=True)
    age = serializers.IntegerField(write_only=True, required=False)
    national_code = serializers.IntegerField(write_only=True, required=False)
    phone_number = serializers.CharField(write_only=True, required=False)


    #Password confirmation
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "full_name", "age", "national_code", "phone_number"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"error": "رمز عبور با تکرار مطابقت ندارد."})
        return data
    
    def create(self, validated_data):

        #  Separating profile fields from the user.
        full_name = validated_data.pop("full_name")
        age = validated_data.pop("age", None)
        national_code = validated_data.pop("national_code", None)
        phone_number = validated_data.pop("phone_number", None)
        validated_data.pop("password2")

        #create user. The (create_user) method hashes the password.
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            password = validated_data["password"]
        )

        #create user profile.
        profile = UserProfile.objects.create(
            user=user,
            full_name=full_name,
            age=age,
            National_code=national_code,
            phone_number=phone_number,
            is_student=True,

        )

        return user