from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    total_score = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in minutes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
