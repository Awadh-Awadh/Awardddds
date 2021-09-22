from django import forms
from .models import Project,Rating,Review
from accounts.models import Profile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
        exclude = ['publisher']

class ReviewForm(forms.ModelForm):
    class Meta:
       model = Review
       fields = '__all__'
       exclude = ('project','reviewer')

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude  = ('user')