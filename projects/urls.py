from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
#   path('projects/',views.all-projects, name = 'all'),
   path('prjectDetail/<int:pk>',views.projectDetail, name = 'projectDetail'),
  path('project-create/',views.upload,name='upload'),
  path('profile/',views.account, name = 'profile')
 ]