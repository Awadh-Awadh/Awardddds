from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.aggregates import Max
from django.db.models.fields.related import ManyToManyField
from accounts.models import Profile

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField
    publisher = models.ForeignKey(Profile, on_delete = models.CASCADE)
    url = models.URLField()
    date_posted = models.DateTimeField(auto_now_add=True)



    def save_project(self):
        return self.save()

    def delete_project(self):
        return self.delete()

    def __str__(self):
        return self.title

class Review(models.Model):
  design = models.CharField(max_length=2)
  userbility = models.CharField(max_length=2)
  content = models.CharField(max_length=2)
  creativity = models.CharField(max_length=2)
  project = ManyToManyField(Project)

  def __str__(self):
    return self.design

