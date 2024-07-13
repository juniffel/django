# 장고 deep하게 go

## 1. 프로젝트 초기설정
```
# startproject만들기
django-admin startproject [프로젝트 이름]

# 앱만들기
python manage.py startapp [앱이름]

# migrate
python manage.py migrate

# superuser만들기
python manage.py createsuperuser

# settings.py 수정
INSTALLED_APPS = [
    #앱 등록
    'exview.apps.ExviewConfig',
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```
```
# 실행해보기
python manage.py runserver
```

## 2. 앱 url추가
```
# 기본앱(mysite) url에 앱 추가하기
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exview/', include('exview.urls')),
]
```
## 3. 인덱스 페이지 만들기
### 앱에 urls.py만들고 인덱스 뷰 url 추가하기
```
# 앱/urls.py에 인덱스 url 추가
from .import views
from django.urls import path

app_name = 'exview'

urlpatterns=[
    path('', views.index, name = 'index'),
```
### 인덱스 뷰 만들기
```
from django.shortcuts import render # 템플릿 사용할 때
from django.http import HttpResponse # 응답을 직접만들때
from django.utils import timezone
# Create your views here.
def index(request):
    # print('클라이언트로 요청받음.')
    # print('=========requset 속성=========')
    # print('scheme:',request.scheme)
    # print('body:',request.body)
    # print('path:',request.path)
    # print('path_info:',request.path_info)
    # print('method:',request.method)
    # print('encoding:',request.encoding)
    # print('content_type:',request.content_type)
    # print('GET:',request.GET)
    # print('POST:',request.POST)
    # print('COOKIES:',request.COOKIES)
    # print('FILES:',request.FILES)
    # print('headers:',request.headers)
    # print('=======================')
    # print('session:', request.session)
    # print('user:', request.user)
    # print('=================Method')
    # print('get_host():', request.get_host())
    # print('get_port():', request.get_port())
    # print('get_full_path():', request.get_full_path())
    # print('get_full_path_info():', request.get_full_path_info())
    # print('build_absolute_uri():', request.build_absolute_uri())
    # print('==================응답')
    # response = HttpResponse('Hello')
    # print('content:', response.content)
    # print('headers:', response.headers)
    # print('charset:', response.charset)
    # print('status_code:', response.status_code)
    # print('items:', response.items())
    # print('======================')
    # return HttpResponse('응답데이터')
    now = timezone.now()
    print('현재 시간:', now)
    return render(request, 'exview/index.html', {'now':now})
```
### 템플릿 만들기
- 장고는 기본적으로 templates 라는 폴더에서 서식을 찾음.
- 앱이 여러개일 경우에 templates 폴더를 잘못찾는 문제가 있음.
- 템플릿 경로 혼동을 막기 위해 templates폴더 안에 앱이름의 폴더 하나 더 만들어서 사용.
- 그래서 경로는 templates/exview/index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Example View 메인함수</h1>
    현재 시간 : {{now}}
    <hr>
    <div id = 'content1'>
        <h3>Request 이해하기(함수형 뷰)</h3>
        <a href="get1/?n1=10&n2=20&n3=hello">get요청</a>
    </div>
</body>
</html>
```
## GET, POST 알아보기 (함수형 뷰)
### exview/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # get요청
    path('get1/', views.get1, name='get1'),
    # 경로 변수 사용
    path('get2/<int:n1>/<int:n2>/<str:n3>/', views.get2, name='get2'),
    # post 요청
    path('post1/', views.post1, name = 'post1'),
    # 경로 변수 사용
    path('post2/<str:msg>/<int:n>/', views.post2, name = 'post2'),
    # getpost 같이 사용 (url은 같게, )
    path('getpost1/', views.getpost1, name = 'getpost1'),
]
```
### views.py
```
def get1(request):
    print(f'GET요청이 들어옴')
    print(f'요청 정보 : {request.GET}')
    print(f'요청 정보에 있는 키들 : {request.GET.keys()}')
    print(f'요청 정보에 있는 값들 : {request.GET.values()}')
    return HttpResponse('get1')

def get2(request,n1,n2,n3):
    print(f'n1:{n1}')
    print(f'n2:{n2}')
    print(f'n3:{n3}')
    return HttpResponse('get2')

def post1(request):
    print('POST1 요청이 들어옴.')
    print(f'요청 정보 : {request.POST}')
    print(f'요청 정보에 있는 키들 : {request.POST.keys()}')
    print(f'요청 정보에 있는 값들 : {request.POST.values()}')
    return HttpResponse('post1')

def post2(request,msg,n):
    print('POST2 요청이 들어옴.')
    print(f'요청 정보 : {request.POST}')
    print(f'요청 정보에 있는 키들 : {request.POST.keys()}')
    print(f'요청 정보에 있는 값들 : {request.POST.values()}')
    print(f'msg:{msg}, n:{n}')
    return HttpResponse('post2')

def getpost1(request):
    print(request.method)
    if request.method == 'GET':
        print('get요청 처리')
    elif request.method == 'POST':
        print('post요청 처리')
    return HttpResponse('getpost1')
```
### 템플릿
```
<h3>Request 이해하기(함수형 뷰)</h3>
<ol>
    <li><a href="get1/?n1=10&n2=20&n3=hello">get요청</a></li>
    <li><a href="get2/10/20/hello/">get요청(2)</a></li>
    <li>
        <form action="post1/", method = post>
            {% csrf_token %}
            <input type="text" name="n1">
            <input type="text" name='n2'>
            <input type="submit" value='요청 및 전송'>
        </form>
    </li>
    <li>
        <form action="post2/hello/123/", method = post>
            {% csrf_token %}
            <input type="text" name="n1">
            <input type="text" name='n2'>
            <input type="submit" value='요청 및 전송'>
        </form>
    </li>
    <li>GETPOST1요청:<a href="getpost1/">getpost1요청</a></li>
    <li>GETPOST2요청:
        <form action="getpost1/", method = post>
            {% csrf_token %}
            <input type="text" name="n1">
            <input type="text" name='n2'>
            <input type="submit" value='요청 및 전송'>
        </form>
    </li>
</ol>
```
## GET, POST 알아보기 (클래스형 뷰)

### urls.py
```
# 클래스형 뷰
# get요청
path('get3/', views.ExamGet3.as_view(), name = 'get3'),
path('get4/<int:n1>/<int:n2>/<str:n3>/', views.ExamGet4.as_view(), name='get4'),
# post 요청
path('post3/', views.ExamPost3.as_view(), name = 'post3'),
path('post4/<str:msg>/<int:n>/', views.ExamPost4.as_view(), name = 'post4'),

# getpost요청
path('getpost2/', views.ExamGetPost2.as_view(), name = 'getpost2')
```
### views.py
```
# 클래스형 뷰
from django.views.generic import View

class ExamGet3(View):
    def get(self, request):
        print(f'get3/요청이 들어옴')
        print(f'요청 정보 : {request.GET}')
        print(f'요청 정보에 있는 키들 : {request.GET.keys()}')
        print(f'요청 정보에 있는 값들 : {request.GET.values()}')
        return HttpResponse('get3')
class ExamGet4(View):
    def get(self, request,n1,n2,n3):
        print(f'get4/요청이 들어옴')
        print(f'n1:{n1}')
        print(f'n2:{n2}')
        print(f'n3:{n3}')
        return HttpResponse('get4')

class ExamPost3(View):
    def post(self, request):
        print('POST3 요청이 들어옴.')
        print(f'요청 정보 : {request.POST}')
        print(f'요청 정보에 있는 키들 : {request.POST.keys()}')
        print(f'요청 정보에 있는 값들 : {request.POST.values()}')
        return HttpResponse('post3')
class ExamPost4(View):
    def post(self, request,msg,n):
        print('POST4 요청이 들어옴.')
        print(f'msg:{msg}, n:{n}')
        return HttpResponse('post4')

class ExamGetPost2(View):
    def get(self, request):
        print('get요청 처리')
        return HttpResponse('getpost2/(GET)')
    def post(self, request):
        print('post요청으로 처리')
        user = request.POST['user']
        pwd = request.POST['pwd']
        if user == pwd:
            print('로그인')
            return HttpResponse('getpost2/(POST)')
        else:
            print('로그인 실패')
            return HttpResponseRedirect('/exview/')
```
### 템플릿
```
<div id = 'content2'>
    <h3>Request 이해하기(클래스형 뷰)</h3>
    <ol>
        <li>GET요청3:<a href="get3/?n1=10&n2=20&n3=hello">get요청3</a></li>
        <li>GET요청4:<a href="get4/10/20/hello/">get요청4</a></li>
        <li>
            <form action="post3/", method = post>
                {% csrf_token %}
                <input type="text" name="n1">
                <input type="text" name='n2'>
                <input type="submit" value='요청 및 전송'>
            </form>
        </li>
        <li>
            <form action="post4/hello/123/", method = post>
                {% csrf_token %}
                <input type="text" name="n1">
                <input type="text" name='n2'>
                <input type="submit" value='요청 및 전송'>
            </form>
        </li>
        <li>GETPOST1요청:<a href="getpost2/">getpost1요청</a></li>
        <li>GETPOST2요청:
            <form action="getpost2/", method = post>
                {% csrf_token %}
                <input type="text" name="user">
                <input type="text" name='pwd'>
                <input type="submit" value='요청 및 전송'>
            </form>
        </li>
    </ol>
</div>
```
## reverse 개념
- [앱이름]:[url이름] 을 사용해 url가져옴.
- url 경로 하드코딩 대신 유연하게 사용하기위해 사용
- url이 변경되어도 urls.py 의 url을 따라가기 때문에 유연하게 대응가능
```
<li>GET요청1:<a href="{% url 'exview:get1' %}">get요청1</a></li>
<li>GET요청2:<a href="{% url 'exview:get2' '100' '200' 'hell' %}">get요청2</a></li>
```

## 템플릿 개요
- html 형태로 UI 담당
- 장고 템플릿 문법을 사용해서 파이썬코드 작성가능 {%%} or {{}}
