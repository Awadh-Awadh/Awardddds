from django.urls import path
from . import views


urlpatterns = [
  path('',views.home, name = 'home'),
  path('projects/',views.projects, name = 'projects'),
  path('prjectDetail/<int:pk>',views.projectDetail, name = 'projectDetail'),
  path('project-create/',views.upload,name='upload'),
  path('profile/',views.account, name = 'profile'),
  path('api/projects/',views.list_all, name = 'all'),
  path('api/project_detail/<int:pk>/',views.project_detail, name = 'detail'),
  path('route/',views.api, name = 'api'),
  path('search/',views.search, name = 'search')
#   path('profiles/', views.profiles, name = 'profiles'),
#   path('profile_detail/<int:pk>/', views.profile_detail, name = 'profile_detail')
 ]