from django.shortcuts import render
from .serializers import ProfileSerializer, ProjectSerializer
from .models import ApiProject, ApiProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api import serializers

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
