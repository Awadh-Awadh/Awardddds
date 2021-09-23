from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
   path('projects/',views.list_all, name = 'all-projects'),
   path('prjectDetail/<int:pk>',views.projectDetail, name = 'projectDetail'),
  path('project-create/',views.upload,name='upload'),
  path('profile/',views.account, name = 'profile')
 ]