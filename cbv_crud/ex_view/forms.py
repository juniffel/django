from django import forms
from django.core.validators import MaxLengthValidator,MinLengthValidator
from .models import Info
class PersonModelForm(forms.ModelForm):
  class Meta:
    model= Info
    fields = ['name','age','intro']


  def clean_name(self):
    print('name 유효성 검증')
    name = self.cleaned_data['name']
    if len(name)<3:
      raise forms.ValidationError('길이가 4보다 길어야 합니다.')
    return name # 무조건 반환해야함

  def clean_age(self):
    print('age 유효성 검증')
    age = self.cleaned_data['age']
    if age>150:
      raise forms.ValidationError('나이는 150 보다 작아야 합니다.')
    return age

  def clean_intro(self):
      print('intro 유효성 검증')
      intro = self.cleaned_data['intro']
      if len(intro)<=5:
        raise forms.ValidationError('소개는 5자 이상이어야 합니둥.')
      return intro
    
  def clean(self):
    print('clean 호출')
    return self.cleaned_data
