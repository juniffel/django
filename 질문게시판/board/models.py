from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.TextField()
    content = models.TextField()

class Answer(models.Model):
    title = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
