from django.contrib import admin
from .models import UserProfile , Student , Teacher

class UserProfileAdmin(admin.ModelAdmin):
    #Specifies which fields will be displayed in the list view
    list_display = ('user', 'get_user_username', 'get_user_email', 'full_name', 'age', 'phone_number', 'profile_img', 'is_admin', 'is_teacher', 'is_student')
    
    #Allows searching by username, email, and full name in the admin panel
    search_fields = ['user__username', 'user__email', 'full_name']


    #fetches the username from the User model
    def get_user_username(self, obj):
        return obj.user.username
    #Set column name to "Username"
    get_user_username.short_description = 'Username'


    #fetches the email from the User model
    def get_user_email(self, obj):
        return obj.user.email
    #Set column name to "Email"
    get_user_email.short_description = 'Email'



class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_full_name', 'courses')

    def get_username(self, obj):
        return obj.profile.user.username
    get_username.short_description = 'Username'

    def get_full_name(self, obj):
        return obj.profile.full_name
    get_full_name.short_description = 'Full Name'



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_full_name', 'teaching_courses')

    def get_username(self, obj):
        return obj.profile.user.username
    get_username.short_description = 'Username'

    def get_full_name(self, obj):
        return obj.profile.full_name
    get_full_name.short_description = 'Full Name'



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)