from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
# 모델에서 유효성 검증 하는법 (보통 모델에서 유효성 검증을 한다고함.)
def validate_name_length(value):
    print('name 유효성 검증')
    if len(value)<4:
      raise ValidationError('길이가 4보다 길어야 합니다.')
    return value # 무조건 반환해야함

def validate_age_scope(value):
  print('age 유효성 검증')
  if value>150:
    raise ValidationError('나이는 150 보다 작아야 합니다.')
  return value


class Person(models.Model):
  name = models.CharField(
    max_length=50,
    null=False,
    validators=[
      validate_name_length,
      MaxLengthValidator(limit_value=20,
                         message='최대 길이 오류'),
    ])
  age = models.IntegerField(
    null=False,
    validators=[
      validate_age_scope,
    ])

  def __str__(self):
    return f'Person[name={self.name},age={self.age}]'
