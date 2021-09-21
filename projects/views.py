from django.shortcuts import render
from .models import Project, Review, Rating
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {
      'projects':projects
    }

    return render(request,'projects/home.html',context)
@login_required
def projectDetail(request,pk):
    project = Project.objects.get(id = pk)
    reviews = Review.objects.all()
    context = {
      'project': project,
      'reviews':reviews
          }
    return render(request, 'projects/detail.html', context)