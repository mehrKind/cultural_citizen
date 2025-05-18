from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    # A profile model that inherits from user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(null=True, blank=True, max_length=150)
    age = models.PositiveIntegerField(null=True, blank=True)
    National_code = models.PositiveIntegerField(max_length=10, unique=True, null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=11, unique=True)
    profile_img = models.ImageField(upload_to="profile_images/", null=True, blank=True)

    #Show roles
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    
    def get_user_username(self):
        return self.user.username
    
    def get_user_email(self):
        return self.user.email
    
    
    @classmethod
    def create(cls, user):
    
        #Create a default UserProfile for a new user.
        profile = cls(user=user, is_student=True)
        profile.save()
        return profile
    
    def __str__(self):
        return f"{self.user.username} Profile"
    


class Student(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="student_profile")
    courses = models.CharField(max_length=500, blank=True, help_text="نام درس‌ها را وارد کنید")

    def __str__(self):
        return f"Student: {self.profile.full_name or self.profile.user.username}"



class Teacher(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="teacher_profile")
    teaching_courses = models.CharField(max_length=500, blank=True, help_text="درس‌هایی که تدریس می‌کند")

    def __str__(self):
        return f"Teacher: {self.profile.full_name or self.profile.user.username}"