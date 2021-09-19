from django.db import models
from projects.models import Project
from accounts.models import Profile

# Create your models here.
class ApiProject(Project):
    def __str__(self):
      return self.title
class ApiProfile(Profile):
    def __str__(self) -> str:
        return self.username