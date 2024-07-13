from django.db import models

# Create your models here.
class Info (models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    intro = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Info[id={self.id}, name={self.name}, age={self.age}, ...]'

