from django.shortcuts import render
from .serializers import ProfileSerializer, ProjectSerializer
from .models import ApiProject, ApiProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def list_all(request):
    '''
    list all projects or create new
    '''
    if request.method == 'GET':
        projects = ApiProject.objects.all()
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
        project = ApiProject.objects.get(id=pk)
    except ApiProject.DoesNotExist:
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
    


@api_view(['GET', 'POST'])
def profiles(request):
    '''
    list all profiles or create new
    '''
    if request.method == 'GET':
        profiles = ApiProfile.objects.all()
        serializer = ProfileSerializer(profiles, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def profile_detail(request,pk):
    '''
    retrieve, update and delete
    '''
    try:
        profile = ApiProfile.objects.get(id=pk)
    except ApiProfile.DoesNotExist:
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