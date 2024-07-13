# 장고 모델 알아보기

## 기본 세팅

### 1.startproject 만들기
```
django-admin startproject mysite
```
### 2.프로젝트 이름 바꾸기
```
mv mysite project03
```

### 3.settings.py

```
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```
### 4.앱 만들기
```
python manage.py startapp ex_model
```
### 5.앱 등록하기
```
INSTALLED_APPS = [
    'ex_model.apps.ExModelConfig',
]
```
### 6.migrate
```
python manage.py migrations

python manage.py migrate
```

### 7.슈퍼유저 생성
```
python manage.py createsuperuser
```

### 8.서버실행
```
python manage.py runserver
```
## 모델 만들기

### 1.models.py
```
class Info (models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    intro = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Info[id={self.id}, name={self.name}, age={self.age}, ...]'
```
### 2.admin에 모델 등록
```
from .models import Info
admin.site.register(Info)
```
### 3.데이터 추가

## shell 다루기

### 1.shell 실행
```
python manage.py shell
```
### 2.데이터 추가1
```
Info(name = '원빈', age = 38, intro='CG')

info = Info(name = '원빈', age = 38, intro='CG')

info.save()
```
### 데이터 추가 2
```
Info.objects.create(name='공유', age=66, intro='도깨비')
```

### 데이터 전체 조회
```
Info.objects.all()
```
### 데이터 일부 조회
```
a = Info.objects.get(id=1)
a.name
a.age
a.regdate

# or
b = Info.objects.get(age==22)
```

### filter
```
Info.objects.filter(name='홍길동')

Info.objects.filter(name__contains='홍', age=25) # 이름에 홍 이 포함되는 데이터

Info.objects.filter(age__lt=40) # 나이가 40보다 작은 데이터

Info.objects.filter(age__lte=40) # 나이가 40보다 작거나 같은 데이터(less than equall)
```
### 필터 변수
- __startswith : ~로 시작하는
- __endswith : ~로 끝나는
- __lt : ~보다 작은
- __gt : ~보다 큰
- __lte : ~보다 작거나 같은
- __gte : ~보다 크거나 같은
- __contains : ~를 포함하는

### and 연산
```
Info.objects.filter(name__contains='홍', age=25)
```
### or 연산
```
from django.db.models.import Q

Info.objects.filter(Q(name__contains='홍'), Q(age=25))
```
### 정렬
```
Info.objects.all().order_by('id') # 오름차순
Info.objects.all().order_by('-id') # 내림차순
```
### 수정1
```
q = Info.objects.get(age=23)
q.age=24 # 나이 수정
q.save()
```

### 수정2
```
Info.objects.filter(age=24).update(name='김길동', age=23)
```
### 삭제
```
Info.objects.filter(name='이성계').delete()
```
