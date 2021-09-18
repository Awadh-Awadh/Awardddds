from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    profilepic = CloudinaryField('image')