from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    total_score = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in minutes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

class QuizResponse(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)
    is_correct = models.BooleanField(default=False)