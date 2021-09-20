from django.urls import path
from . import views

urlpatterns = [
  path('projects/',views.list_all, name = 'all'),
  path('project_detail/<int:pk>/',views.project_detail, name = 'detail'),
  path('profiles/', views.profiles, name = 'profiles'),
  path('profile_detail/<int:pk>/', views.profile_detail, name = 'profile_detail')
]