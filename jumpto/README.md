# 점프 투 장고 QnA 게시판(pybo) 만들기
## 사이트 개요
첫페이지: 질문의 제목을 나열한 형태의 게시판을 만든다.
<img src="readmeimgs/스크린샷 2024-07-20 17-24-26.png" width="50%" height="30%"/>
상세 페이지 : 첫 페이지의 제목에 링크를 통해 이동, 질문에 대한 상세한 내용을 표시한다.
<img src="readmeimgs/스크린샷 2024-07-20 17-32-43.png" width="50%" height="30%"/>
답변등록 : 상세페이지에서 입력창을 만들어 답변을 등록하고 버튼을 누르면 POST요청을 보내 등록한 답변을 생성한후에 다시 redirect한다.
<img src="readmeimgs/스크린샷 2024-07-20 17-38-30.png" width="50%" height="30%"/>
질문등록 : 첫 페이지에서 질문등록 버튼을 통해 이동하고, 제목, 내용을 입렫받아 등록버튼을 통해 POST요청을 보내고 첫페이지를 redirect
<img src="readmeimgs/스크린샷 2024-07-20 17-40-11.png" width="50%" height="30%"/>
답변삭제 : 상세 페이지에서 삭제 버튼을 누르면 답변의 작성자를 확인하고 작성자가 일치하면 '정말로 삭제 하시겠습니까?'라는 메시지를 출력한 후 확인을 누르면 모델.delete 이용해 답변을 삭제한다.
<img src="readmeimgs/스크린샷 2024-07-20 17-38-30.png" width="30%" height="30%"/>
질문 삭제 : 첫 페이지에서 질문의 삭제 버튼을 클릭하면 답변의 작성자를 확인하고 작성자가 일치하면 '정말로 삭제 하시겠습니까?'라는 메시지를 출력한 후 확인을 누르면 모델.delete 이용해 답변을 삭제한다.
불일치 하면 '버튼을 안보이게 하거나, 작성자가 아닙니다란 메세지를 띄운다.
<img src="readmeimgs/스크린샷 2024-07-20 17-38-30.png" width="30%" height="30%"/>
질문,답변 수정 :

### 장고 쉘에서 모델 CRUD
```
python manage.py shell

# 임포트
from [app].models import [모델 클래스 명]

# 생성
c= 클래스명(필드명='', 필드명='')

# 저장
c.save()

# 전체 조회
클래스명.objects.all()

# filter 조회 => QuerySet반환,(여러건 조회 할 때를 대비해서 이러게 만든듯)
클래스명.objects.filter(id=1)

# get 조회 => 객체반환 (한 건만 조회할때 를 대비해서 이렇게 만든듯)
클래스명.objects.get(id=1)

# 수정
u = 클래스명.objects.get(id=1)
u.필드명 = ''
u.save()

# 삭제
d = 클래스명.objects.get(id=1)
d.delete()

# 참조키로 조회
q = 클래스명.objects.get(id=1)
q.클래스명_set.all()
```

### 관리자(슈퍼유저) 생성 및 admin에 모델 등록
```
# 터미널
python manage.py createsuperuser

# admin.py
from django.contrib import admin
from .models import 모델명

# admin.site.register(모델명)

# 모델 검색필드 적용
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
```
### 템플릿 태그

```
# 조건문
{% if 조건식 %}
{% endif %}

# for
{% for i in iterator %}
{% endfor %}

# forloop.counter : 순서 1부터 시작
# forloop.counter0 : 순서 0부터 시작
# forloop.first : 첫번째 순서이면 True
# forloop.last : 마지막 순서이면 True

# 변수
{{변수 명}}
```


## 네비게이션 바
- 부트스트랩에서 네이게이션바 가져와서 navbar.html에 저장
- 부트스트랩js 적용 (반응형 디자인)
- include로 base.html에 적용
  ```
   <!-- 네비게이션 바 적용 -->
    {% include 'navbar.html' %}

    <!-- 콘텐츠 영역 -->
    {% block content %}{% endblock content %}

    <!-- Bootstrap JS -->
    <script src="{% static 'bootstrap.min.js' %}"></script>
  ```
- 화면
<img src="readmeimgs/스크린샷 2024-07-22 15-09-51.png" width="50%" height="30%"/>

## 페이지네이터
-  장고에서 페이지네이터 가져오기
-  인덱스뷰 에 페이지네이터 적용
  ```
  from django.core.paginator import Paginator # 페이징
    def index(request):
        # 페이지 가져오기
        page = request.GET.get('page','1')
        # 생성일 역순으로 질문 목록이 담긴 리스트
        question_list = Question.objects.order_by('create_date')
        # 페이지네이터 : 질문을 10개씩 묶은 페이지 범위 객체 : range(1,32)
        paginator = Paginator(question_list,10)
        # 페이지 객체 : 페이지 번호에 해당하는 질문 리스트 10개
        page_obj = paginator.get_page(page)
        template_name = 'pybo/question_list.html'
        context = {'question_list':page_obj}
        return render(request, template_name, context)
  ```

## 템플릿 필터
- templatetags/pybo_filter.py : 게시물 번호 출력계산을 위한 sub 정의
```
from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg
```
- question_list.html 에 적용 : 번호 = 전체건수 - 시작인덱스 - 현재인덱스 + 1
    ```
    {% extends 'base.html' %}
    {% load pybo_filter %}
    {% block content %}
    <div class="container my-3">
        <table class="table">
            <thead>
            <tr class="table-dark">
                <th>번호</th>
                <th>제목</th>
                <th>작성일시</th>
            </tr>
            </thead>
            <tbody>
            {% if question_list %}
            {% for question in question_list %}
            <tr>
                <td>
                    <!-- 번호 = 전체건수 - 시작인덱스 - 현재인덱스 + 1 -->
                    {{ question_list.paginator.count|sub:question_list.start_index|sub:forloop.counter0|add:1 }}
                </td>
    ```
## 답변 개수 표시
- question_list.html
    ```
    {% if question.answer_set.count > 0 %}
    <span class="text-danger small mx-2">{{ question.answer_set.count }}</span>
    {% endif %}
    ```

## 로그인, 로그아웃, 회원가입
- loginview사용 : get, post요청에 따라 자동으로 처리, 인증절차(아이디,비밀번호 매칭) 자동처리
-
