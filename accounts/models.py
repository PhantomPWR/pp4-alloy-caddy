from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    Extends base user model to specify email as unique
    """
    email = models.EmailField(unique=True)
