from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.
class CustomUSer(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    profilepic = CloudinaryField('image')
    bio = models.TextField()
    contact= models.CharField(max_length=10)