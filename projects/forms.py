from django import forms
from .models import Project,Rating,Review


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
        exclude = ['publisher']