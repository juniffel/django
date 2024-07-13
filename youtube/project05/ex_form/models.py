from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
# 모델에서 유효성 검사
def clean_name(value):
    print("name 유효성 검증")
    if len(value)>4:
        raise ValidationError('길이 오류')
    return value

    self.cleaned_data['name']

def clean_age(value):
    print("age 유효성 검증")
    if not 0<value<150:
        raise ValidationError('나이 오류')
    return value

    self.cleaned_data['age']

class Person(models.Model):
    name = models.CharField(
        max_length=20,
        null=False,
        validators=[
            clean_name,
        ])
    age = models.IntegerField(
        null=False,
        validators=[
            clean_age,
        ])

    def __str__(self):
        return f'Person[id={self.id}, name={self.name},age={self.age}]'
