from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUSer, Profile

# Register your models here.
class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUSer
    list_display = ['first_name','last_name','username','email']

admin.site.register(CustomUSer, CustomAdmin)
admin.site.register(Profile)