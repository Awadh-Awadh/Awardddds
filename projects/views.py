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
    project = Project.objects.get(id = pk)
    reviews = Review.objects.filter(project = project).all()
    rating = Rating.objects.filter(project = project )



    '''
    If you are using values_list() with a single field, you can use 
    flat=True to return a QuerySet of single values instead of 1-tuples:
    
    '''
    # design = Rating.objects.filter(project = project).aggregate(Avg('design'))
    # userbility = Rating.objects.filter(project = project).aggregate(Avg('userbility'))
    # creativity = Rating.objects.filter(project = project).aggregate(Avg('creativity'))
    # content = Rating.objects.filter(project = project).aggregate(Avg('content'))
    # av_total = float(int(design['design__avg']) + int(userbility['userbility__avg']) + int(creativity['creativity__avg']) + int(content['content__avg']))
    # score = round(av_total/4, 2)
    
   
    if request.method =='POST':
       
        rev_form = ReviewForm(request.POST)
        rat_form = RatingForm(request.POST)
        
        if rev_form.is_valid() and rat_form.is_valid():
            obj = rev_form.save(commit = False)
            rating = rat_form.save(commit = False)
            obj.project= project
            rating.project = project
            obj.reviewer = request.user
            rating.rated_by = request.user
            rev_form.save()
            rat_form.save()            
            return redirect('projectDetail')
    else:
        
        rev_form = ReviewForm()
        rat_form = RatingForm()

    
    context = {
        'project': project,
        'reviews':reviews,
        'rev_form':rev_form,
        'rat_form':rat_form,
        
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
            return redirect(account)
    else:
        form = EditProfile()

    context = {
      'profile':profile,
      'form':form
    }
    return render(request, 'projects/account.html',context)
@login_required
def list_all(request):
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