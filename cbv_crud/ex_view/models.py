from django.db import models

class Info(models.Model):
  name = models.CharField( max_length=50)
  age = models.IntegerField()
  intro = models.TextField()

  def __str__(self):
    return f"id:{self.id} | 이름:{self.name} - 나이:{self.age}"
