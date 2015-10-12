from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ['user', 'grade', 'class_of', 'balance',  'pub_date']
    list_display = ['username', 'user_email','first_name','last_name', 'grade', 'class_of', 'balance',  'pub_date']

    def username(self,obj):
        return obj.user.username

    def first_name(self,obj):
        return obj.user.first_name

    def last_name(self,obj):
        return obj.user.last_name

    def user_email(self,obj):
        return obj.user.email


admin.site.register(UserInfo, UserAdmin)
