from rest_framework import serializers
from .models import Profile, Project


class ProjectSerializer(serializers.Serializer):
     class Meta:
        model = Project
        fields = '__all__'

class ProfileSerializer(serializers.Serializer):
     class Meta:
        model = Profile
        fields = '__all__'