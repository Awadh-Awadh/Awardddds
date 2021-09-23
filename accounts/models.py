from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings



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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.save()

    def __str__(self):
        self.contact