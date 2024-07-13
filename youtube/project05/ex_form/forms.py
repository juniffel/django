from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator

def my_validator(value):
    if value<0:
        raise forms.ValidationError('나이는 음수를 사용할 수 없음.')
    return value

class PersonForm(forms.Form):
    name = forms.CharField(
        label = '이름',
        max_length=200,
        required = True,
        validators = [
            MaxLengthValidator(limit_value=20),
            MinLengthValidator(limit_value=4)
            ],
        )
    age = forms.IntegerField(
        label='나이',
        required = True,
        )

    def clean_age(self):
        age = self.cleaned_data.get('age',0)
        if age>150:
            raise forms.ValidationError('값이 범위를 벗어남.')
        return age


from .models import Person
class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']

        def clean_name(self):
            print("name 유효성 검증")
            name = self.cleaned_data['name']
            if len(name)>4:
                raise forms.ValidationError('길이 오류')
            return name

            self.cleaned_data['name']

        def clean_age(self):
            print("age 유효성 검증")
            age = self.cleaned_data['age']
            if 0<age<150:
                raise forms.ValidationError('나이 오류')
            return age

            self.cleaned_data['age']
