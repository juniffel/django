# 장고 도큐먼트 튜토리얼

## 장고 앱 작성하기 part1

### 파이썬, 장고 설치확인
```
python -m django --version
```
### start프로젝트 만들기
```
django-admin startproject 프로젝트 이름(test안됨!)
```
#### start프로젝트 내부
- file:mysite/ 디렉토리 밖은 프로젝트를 담는 공간입니다. 그 이름은 Django 와 아무 상관이 없으니, 원하는 이름으로 변경해도 됩니다.
- manage.py: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티 입니다. manage.py 에 대한 자세한 정보는 django-admin and manage.py 에서 확인할 수 있습니다.
- mysite/ 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여, (mysite.urls 와 같은 식으로) 프로젝트의 어디서나 Python 패키지들을 임포트할 수 있습니다.
- mysite/__init__.py: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일입니다. Python 초심자라면, Python 공식 홈페이지의 패키지를 읽어보세요.
- mysite/settings.py: 현재 Django 프로젝트의 환경 및 구성을 저장합니다. Django settings에서 환경 설정이 어떻게 동작하는지 확인할 수 있습니다.
- mysite/urls.py: 현재 Django project 의 URL 선언을 저장합니다. Django 로 작성된 사이트의 “목차” 라고 할 수 있습니다. URL dispatcher 에서 URL 에 대한 자세한 내용을 읽어보세요.
- mysite/asgi.py: 현재 프로젝트를 서비스하기 위한 ASGI-호환 웹 서버의 진입점입니다. 자세한 내용은 ASGI를 사용하여 배포하는 방법 를 참조하십시오.
- mysite/wsgi.py: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다. WSGI를 사용하여 배포하는 방법를 읽어보세요.

### 장고 서버 실행
```
python manage.py runserver

# 포트번호 바꾸기
python manage.py runserver [포트번호]

# 외부접속 가능
python manage.py runserver 0.0.0.0:[포트번호]

# 포트 연결 확인
lsof -i:8000

#포트 연결 끊기
kill -9 [PID]
```
### 서버주소
- http://127.0.0.1:8000/

### 앱만들기
```
python manage.py startapp polls
```
### 뷰 작성하기
```
# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
### urlconf생성(url 매핑)
- polls/urls.py 만들기
```
# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # 빈 url 요청이 들어오면 index뷰로 가라.
    path("", views.index, name="index"),
]
```
```
# mysite/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # polls/ url이 오면 polls 폴더로 가서 찾아라.
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```
## 튜토리얼 part2

### 데이터베이스 설치
- mysite/settings.py
- 튜토리얼에서는 sqlite를 사용하기때문에 설치, 설정x but, 실제피로젝트는 postgresql 이나mysql을 사용하기때문에 설정필요

### TIME_ZONE설정
```
TIME_ZONE = 'Asia/Seoul'
```

### 모델만들기
- ORM(Object Relation Mapping)을 사용해서 sql을 다루지 않고 파이썬 코드로 작성할수 있게 해준다.
```
# polls.models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
### sql 간단요약
#### Primary Key(PK)
-
#### FK : Forigner Key
- 참조키 : 지정한 모델의 PK를 참조

### 테이블 예시
- 돈까스는 없는 PK를 참조하므로 무결성의 오류이다.
- CASCADE(종속, 연쇄적인) : PK 모델을 삭제하면 참조키들도 모두 삭제된다.
|id(pk)|question_text|pub_date|
|------|---|---|
|1|좋아하는 음식은?|20240326|
|테스트1|테스트2|테스트3|
|테스트1|테스트2|테스트3|

|id(pk)|question(fk)|choice_text|votes|
|------|---|---|---|
|1|1|김밥|0|
|1|2|비빔면|0|
|1|3|육회|0|
|2|4|돈까스|0|
### 모델활성화
```
# settings.py
INSTALLED_APPS = [
    "polls.apps.PollsConfig", # <=여기
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```
### 마이그레이션
```
# 수정된 모델이 있는지 확인하고 django에 알림
python manage.py makemigrations polls

# 데이터베이스에 어떤 테이블이 만들어질지 확인.
python manage.py sqlmigrate polls 0001

# 데이터 베이스에 모델과 관련된 테이블 생성
python manage.py migrate
```

### API 가지고 놀기
```
python manage.py shell

>>> from polls.models import Choice, Question

>>> Question.objects.all()
<QuerySet []>

>>> from django.utils import timezone

>>> q = Question(question_text="What's new?", pub_date=timezone.now())

>>> q.save()

>>> q.id
1

>>> q.question_text
"What's new?"

>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

>>> q.question_text = "What's up?"
>>> q.save()

>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```
### 모델 수정
```
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # ...
    # 추가
    def __str__(self):
        return self.question_text
    # 추가
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # ...
    # 추가
    def __str__(self):
        return self.choice_text
```
- 수정후 확인
```
>>> from polls.models import Choice, Question

>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

>>> Question.objects.get(pk=1)
<Question: What's up?>

>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

>>> q = Question.objects.get(pk=1)

>>> q.choice_set.all()
<QuerySet []>

>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

>>> c.question
<Question: What's up?>

>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```
### 관리자 생성하기
```
python manage.py createsuperuser
유저이름 : 입력
이메일 : 입력
비밀번호 : 입력

# 서버시작
python manage.py runserver
```
-  (http://127.0.0.1:8000/admin/)이동

### 관리자 사이트 언어 변경
```
# settings.py
LANGUAGE_CODE = ko-kr
```
### 관리 사이트에 polls앱 등록하기
```
# polls/admin.py
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
## part3

### 장고 MTV 패턴

1. 사용자 url 검색을 통한 HTTP 요청 ->
2. urls.py에서 해당하는 url과 매핑된 뷰로 이동->
3. 뷰에서 models를 통해 데이터가져오기
4. 뷰에서 템플릿을 통해 서식가져오기
5. HTTP 응답
6. 브라우저에 렌더링

### 뷰 추가하기
```
# polls/views.py

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
### url 연결
```
# polls.urls
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
### 뷰에 index 수정
```
# polls/views.py
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```

### 뷰에 index 수정2(html추가)
```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
### 뷰에 index 수정3 (render 사용하기)
```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```
### 404에러 일으키기
```
# polls/views.py
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```
### 404 일으키기 수정(get_object_or_404() 사용)
```
from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

### 여러앱을 사용하기위해 url 이름 공간 정하기
```
# polls/urls.py
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
### 템플릿 수정
```
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
## part4
### detail뷰 폼만들기
```
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```
### url conf
```
# polls/urls.py
path("<int:question_id>/vote/", views.vote, name="vote"),
```
### vote 뷰 만들기
```
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

### vote 뷰 리다이렉트
```
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```
### vote 페이지
```
# polls/templates/polls/results.html
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```
### URLconf 수정
```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

### views 수정 (제네릭 기반 클래스)
```
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # same as above, no changes needed.
    ...
```
