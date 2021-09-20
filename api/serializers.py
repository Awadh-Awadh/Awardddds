from rest_framework import serializers
from .models import ApiProfile, ApiProject


class ProjectSerializer(serializers.Serializer):
     class Meta:
        model = ApiProject
        fields = '__all__'

class ProfileSerializer(serializers.Serializer):
     class Meta:
        model = ApiProfile
        fields = '__all__'