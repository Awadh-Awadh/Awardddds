from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {
      'projects':projects
    }

    return render(request,'projects/home.html',context)

def projectDetail(request,pk):
    project = Project.objects.get(id = pk)
    context = {
      'project': project
    }
    return render(request, 'projects/detail.html', context)