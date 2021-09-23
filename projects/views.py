from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import Project, Review, Rating,Profile
from django.contrib.auth.decorators import login_required
from .forms import UploadForm,ReviewForm, EditProfile,RatingForm
from django.db.models import Avg
from .serializers import ProfileSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {
      'projects':projects
    }

    return render(request,'projects/home.html',context)
@login_required
def projectDetail(request,pk):
    project = Project.objects.get(pk = pk)    
    reviews = Review.objects.filter(project = project).all()  
    ratings = Rating.objects.filter(project=project) 
    design = 0
    score = 0
    userbility = 0
    creativity = 0
    content = 0
    if request.method =='POST':
       
        rev_form = ReviewForm(request.POST)
        rat_form = RatingForm(request.POST)
        if rev_form.is_valid():
            obj = rev_form.save(commit = False)
            obj.project= project
            obj.reviewer = request.user
            rev_form.save()
        if rat_form.is_valid():
            rating = rat_form.save(commit = False)            
            rating.project = project            
            rating.rated_by = request.user           
            rat_form.save()  
            design = rat_form.cleaned_data['design'] 
            userbility = rat_form.cleaned_data['userbility']
            creativity = rat_form.cleaned_data['creativity']
            content = rat_form.cleaned_data['content']
            total = design + userbility + creativity +content
            score = total// 4

            

            print(design)        
            
    else:
        
        rev_form = ReviewForm()
        rat_form = RatingForm()

  
    context = {
        'project': project,
        'reviews':reviews,
        'rev_form':rev_form,
        'rat_form':rat_form,
        'score':score,
        'design':design,
        'userbility':userbility,
        'creativity':creativity,
        'content': content
        
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
      # print(request.user)
      return redirect('home')
  else:
      form = UploadForm()
      context= {
          'form':form
        }


  return render(request, 'projects/upload.html', context)

@login_required
def account(request):
    loggedin_user=request.user
    profile = Profile.objects.get(user=loggedin_user)
    if request.method == 'POST':
        form = EditProfile(request.POST,
        request.FILES, 
        instance = request.user)

        if form.is_valid():
            # obj = form.save(commit = False)
            # obj.user = user
            form.save()
            return redirect('projects')
    else:
        form = EditProfile()

    context = {
      'profile':profile,
      'form':form
    }
    return render(request, 'projects/account.html',context)
@login_required
def projects(request):
    projects = Project.objects.all()
    context = {
      'projects':projects}
    return render(request, 'projects/home.html',context)




    #API
@api_view(['GET', 'POST'])
def list_all(request):
    '''
    list all projects or create new
    '''
    if request.method == 'GET':
        projects = Project.objects.all()
        print(projects)
        serializer = ProjectSerializer(projects, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def project_detail(request,pk):
    '''
    retrieve, update and delete
    '''
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    if request.method =='GET': 
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProjectSerializer(project,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# @api_view(['GET', 'POST'])
# def profiles(request):
#     '''
#     list all profiles or create new
#     '''
#     if request.method == 'GET':
#         profiles = ApiProfile.objects.all()
#         serializer = ProfileSerializer(profiles, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProfileSerializer(data = request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def profile_detail(request,pk):
    '''
    retrieve, update and delete
    '''
    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    if request.method =='GET': 
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)