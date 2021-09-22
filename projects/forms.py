from django import forms
from .models import Project,Rating,Review
from accounts.models import Profile
from django.db.models import Avg


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
        exclude  = ('user',)
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
        exclude = ('project','rated_by')
       