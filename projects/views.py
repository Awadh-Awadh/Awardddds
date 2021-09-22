from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import Project, Review, Rating,Profile
from django.contrib.auth.decorators import login_required
from .forms import UploadForm,ReviewForm

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
    reviews = Review.objects.filter(project = project).all()
    
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.project= project
            obj.reviewer = request.user
            form.save()
    else:
        form = ReviewForm()
    context = {
        'project': project,
        'reviews':reviews,
        'form':form
          }
    return render(request, 'projects/detail.html', context)


@login_required
def upload(request):
  if request.method == 'POST':
    form = UploadForm(request.POST,request.FILES)
    if form.is_valid():
      publisher = Profile.objects.get(user = request.user)
      obj = form.save(commit = False)
      obj.publisher = publisher
      form.save()
      print(request.user)
      return redirect('home')
  else:
      form = UploadForm()
      context= {
          'form':form
        }


  return render(request, 'projects/upload.html', context)


def account(request):
    loggedin_user=request.user
    profile = Profile.objects.filter(user=loggedin_user)

