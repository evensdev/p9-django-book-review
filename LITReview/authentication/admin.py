from django.contrib import admin
from .models import User
from .forms import SignupForm
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    model = User
    add_form = SignupForm
    list_display = ('username', 'email', 'first_name', 'profile_photo')


admin.site.register(User, UserAdmin)
