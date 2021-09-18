from django.db import models
from cloudinary.models import CloudinaryField
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
