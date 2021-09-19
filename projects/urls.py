from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
#   path('projects/',views.all-projects, name = 'all'),
#   path('prjectDetail/',views.detail, name = 'project-detail'),
#   path('project-create/',views.upload,name='upload')
 ]