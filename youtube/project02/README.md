# 템플릿 개요
- html 형태로 UI 담당
- 장고 템플릿 문법을 사용해서 파이썬코드 작성가능 {%%} or {{}}

## 장고의 템플릿 검색 순서 이해하기
- settings.py 에서 템플릿 베이스 경로 설정
```
'DIRS': [BASE_DIR, 'templates',],
```
- templates라는 폴더에서 먼저 해당하는 HTML 파일을 찾고 없으면 앱 내에서 찾음.
- 그래서 경로혼동이 올수 있는데 이것을 막기위해 앱에서 템플릿 폴더내에 앱이름의 폴더를 하나 더 만들고 그안에 html파일을 작성


## 템플릿 변수
- view 에서 context변수에 있는 변수를 html 에서 사용가능

## 없는 변수 접근시 작동 설정
- settings.py
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            <!-- 이부분 설정-->
            'string_if_invalid':'Unknown Value!!',
            <!-- 이부분 설정-->
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## ex02 템플릿 필터
- {{변수명|키워드(필터)}}

## ex03 템플릿 태그 for 사용방법
- 템플릿 태그 : {% %}사용
```
{% for name in name_list %}
    <li>{{name}}</li>
{% endfor %}

```
## ex04 템플릿 태그 if 사용방법
```
{% if 조건문 %}
{% else %} or {% elif %}
{% endif %}
```
## ex05 템플릿 태그 url 이해하기
{% url %}

## ex06 템플릿 태그 csrf 이해하기
- cross site request forgery
- 보안 용도
- 토큰값을 사용해 데이터의 무결성 검증
- post 요청에서는 {% csrf_token%}을 넣어줘야 한다.

## ex07 템플릿 태그 with 이해하기
- 잠시 기억해둘값을 넣어놓음.
```
{% with a=value %}
a:[{{a}}] <br>
{% endwith %}
a:[{{a}}] <br>
```
## ex08 템플릿 태그 comment(주석) 사용하기
- 싱글라인 {# 주석 #}
- 여러줄 {% comment %}
```
{% comment '주석입니다.'%}
{% endcomment %}
<!-- 이 HTML 주석은 브라우저 개발자도구에서 볼수 있음 주의 -->
```
## ex09 템플릿 태그 HTMLescape 사용하기
- 문자열에 있는 HTML 태그가 브라우저에서 해석되지 않도록 특수문자로 변환하는것
```
# escape를 끄고 싶을 때
{% autoexcape:off %}
{% endautoescape %}
# 또는
{{HTML|safe}}

```
## 템플릿 재사용
- 템플릿 상속
- base.html을 통해 기본 템플릿 생성
- {% block %} {% endblock %}을 재사용 가능성이 있는 부분에 삽입
- 다른 HTML 파일에서 base.html으 상속받아 block 부분만 고쳐 사용
- 상속 {% extends 'ex_template/base.html'%}
- 블록 재정의 {% block title %} Index {% endblock %}


## 정적파일 추가
- 앱 폴더 안에 static/앱이름/파일 순으로 만든다.
- html 파일에 아래와 같이 코딩하여 사용
```
{% load static %}
<img src="{% static 'ex_template/ggobugi.gif' %}"alt="" width= '400px', height = '300px'>
```
- settings.py에 static경로를 지정해 놓을 수 있음.
```
STATIC_URL = 'static/'
```
## 정적 파일 경로 설정
- settings.py
```
import os
STATIC_DIR = os.path.join(BASE_DIR, 'static_dir')

STATICFILES_DIRS = [
    STATIC_DIR,
]
```
## 혹시나 정적 파일이 반영이 안될 때
- 캐시 삭제 해보기


## 장고 모델은 project03번에서 계속..
