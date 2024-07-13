# 장고 폼

## 기본세팅
- 스타트 프로젝트
- 이름바꾸기(project05)
- 스타트 앱(ex_form)
- settings [앱등록, 언어, 시간 설정]
- 마이그레이트
- 슈퍼유저
- 서버실행
- url등록


## forms.py
- 모델 정의와 비슷
- html form태그를 대신 만들어줌.
- 유효성 검증을 위해 사용할..껄? 아마도?
```
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
```

## 클래스뷰

