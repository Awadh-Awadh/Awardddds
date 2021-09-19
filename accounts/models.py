from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class CustomUSer(AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username






class Profile(models.Model):
    profilepic = CloudinaryField('image')