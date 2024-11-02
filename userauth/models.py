from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/',null=True,blank=True)

    #set this field to required
    REQUIRED_FIELDS = ['first_name','last_name','email']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
