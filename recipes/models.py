from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GuestProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.nickname or 'Unnamed Guest'} ({self.user.username})"
