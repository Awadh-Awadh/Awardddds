from django.contrib import admin
from .models import ApiProfile, ApiProject
# Register your models here.
admin.site.register(ApiProject)
admin.site.register(ApiProfile)