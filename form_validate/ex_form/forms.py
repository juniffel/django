from django import forms
from django.core.validators import MaxLengthValidator,MinLengthValidator
# 클래스 밖에서 검증기 만들기 => 클래스에서 등록해줘야 작동
def my_validator(value):
  if value<0:
    raise forms.ValidationError('나이는 음수를 사용할 수 없습니다.')
  return value

class PersonForm(forms.Form):
  name = forms.CharField(
      label = '이름',
      max_length=20,
      required=True,
      # 검증기 : is_valid가 호출될때 적용
      validators=[
        MaxLengthValidator(limit_value=20),
        MinLengthValidator(limit_value=4)
      ]
    )

  age = forms.IntegerField(
    label='나이',
    required=True,
    validators=[
      my_validator
    ]
    )

  # 검증기 직접 만들기, clean_필드명으로 만듬,알아서 is_valid호출시 적용됨
  def clean_age(self):
    age = self.cleaned_data.get('age',0)
    if age>150:
      raise forms.ValidationError('값이 범위를 벗어났다.')
    return age # 반드시 값 확인

# 모델 폼 클래스 사용법
from .models import Person
class PersonModelForm(forms.ModelForm):
  class Meta:
    model= Person
    fields = ['name','age']


  def clean_name(self):
    print('name 유효성 검증')
    name = self.cleaned_data['name']
    if len(name)<4:
      raise forms.ValidationError('길이가 4보다 길어야 합니다.')
    return name # 무조건 반환해야함

  def clean_age(self):
    print('age 유효성 검증')
    age = self.cleaned_data['age']
    if age>150:
      raise forms.ValidationError('나이는 150 보다 작아야 합니다.')
    return age

  def clean(self):
    print('clean 호출')
    return self.cleaned_data
