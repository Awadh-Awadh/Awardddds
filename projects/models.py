from django.db import models
from cloudinary.models import CloudinaryField
from accounts.models import Profile
from django.conf import settings

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField()
    publisher = models.ForeignKey(Profile, on_delete = models.CASCADE)
    url = models.URLField(blank=True)
    location = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)



    def save_project(self):
        return self.save()

    def delete_project(self):
        return self.delete()

    def __str__(self):
        return self.title

class Review(models.Model):
 project = models.ForeignKey(Project, on_delete = models.CASCADE)
 review = models.TextField()
 reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
 date_reviewed = models.DateTimeField(auto_now_add=True)
 def __str__(self):
    return self.reviewer.username

class Rating(models.Model):
    design = models.IntegerField()
    userbility = models.IntegerField()
    creativity = models.IntegerField
    content = models.IntegerField()
    score = models.IntegerField(default = 0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return 