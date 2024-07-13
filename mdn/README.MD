# 장고 공부 시작

## 장고란?
- 파이썬 기반의 웹프레임워크

## 장고의 로직 작동 방식

1. HTTP요청(request)
2. urls.py(url확인)
3. view.py(해당하는 view로 접근)
4. models.py(데이터 처리), templates(웹서식 처리 ,HTML)
5. HTTP응답(response)

## 개발환경설정
### python 설치
```
sudo apt install python3-pip
```
### 가상환경 만들기
```
sudo pip3 install virtualenvwrapper
```
### .bashrc파일 찾기 및 수정
- ls -al 로 home에 숨겨진 .bashrc파일 찾기
- vim .bashrc로 파일 열어서 하단에 아래 명령어 추가
    ```
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh
    ```
- source ~/.bashrc 로 업데이트
### 가상환경 생성하고 싶은 디렉토리로 이동(cd ~)

### 가상환경 명령어
- mkvirtualenv 가상환경이름
- deactivate — 활성화된 파이썬 가상 환경을 비활성화합니다.
- workon — 사용가능한 가상 환경 목록을 보여줍니다.
- workon name_of_environment — 특정 파이썬 가상 환경을 활성화합니다.
- rmvirtualenv name_of_environment — 특정 환경을 제거합니다.
### 장고설치 및 확인
```
pip3 install django

python3 -m django --version
```
### 장고 스타트 프로젝트 설치
```
django-admin startproject 디렉토리 명
```
### 장고 서버 실행
```
python3 manage.py runserver
```
- http://127.0.0.1:8000로 이동해서 장고 실행 확인

## 지역도서관 프로젝트

### 스타트 프로젝트 만들기
```
django-admin startproject locallibrary
cd locallibrary
```
### 디렉토리 역할
- __init__.py는 빈 파일입니다. 이 파일은 파이썬에게 이 디렉토리를 하나의 파이썬 패키지로 다루도록 지시합니다.
- settings.py는 웹사이트의 모든 설정을 포함하고 있습니다. 이 파일에는 우리가 만드는 모든 어플리케이션, 정적 파일의 위치, 데이터베이스 세부 설정 등을 등록합니다.
- urls.py는 사이트의 URL과 뷰의 연결을 지정해줍니다. 여기에는 모든 URL 매핑 코드가 포함될 수 있지만, 특정한 어플리케이션에 매핑의 일부를 할당해주는 것이 일반적입니다.
- wsgi.py는 당신의 장고 어플리케이션이 웹서버와 연결 및 소통하는 것을 돕습니다. 당신은 이것을 표준 형식(boilerplate)으로 다뤄도 무방합니다.
- asgi.py는 Python 비동기 웹 앱과 서버가 서로 통신하기 위한 표준으로, WSGI의 비동기 후속 제품으로 자리매김합니다. 여기서 WSGI는 동기 Python 앱에 대한 표준을 제공하고 ASGI는 WSGI를 통해 비동기 및 동기 앱 모두에 대한 표준을 제공합니다. 이전 버전과의 호환성 구현, 다중 서버 및 애플리케이션 프레임워크.
- manage.py는 어플리케이션을 생성하고, 데이터베이스와 작업하고, 그리고 개발 웹 서버를 시작하기 위해 사용됩니다.

### 카탈로그 앱 만들기
```
python3 manage.py startapp catalog
```
- manage.py가 있는 폴더내 에서
- python3 manage.py startapp catalog 실행
- migrations 폴더 — 모델을 수정할 때 마다 자동으로 데이터베이스를 업데이트하는 것을 가능하게 해 줄 마이그레이션 파일들을 저장할 폴더
- __init__.py — 장고/파이썬이 폴더를 파이썬 패키지로 인식하게 할 빈 파일입니다. 또한 프로젝트의 다른 부분에서 객체(object)를 사용할 수 있게 합니다.

### 어플리케이션 등록
- /localibrary/settings.py
- 어플리케이션을 프로젝트에 등록
    ```
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog.apps.CatalogConfig', # 여기
    ]
    ```
- 타임존 설정 : TIME_ZONE = 'Asia/Seoul'
- SECRET_KEY : 이것은 장고의 웹사이트 보안 전략의 일부로 사용되는 비밀키입니다. 만약 이 코드를 개발 과정에서 보호하지 않는다면 제품화(production) 과정에서 다른 코드(아마 환경변수나 파일에서 읽어오는)를 사용해야 할 것입니다.
- DEBUG : 이것은 에러가 발생했을 때 HTTP 상태코드 응답 대신 디버깅 로그가 표시되게 합니다. 디버깅 정보는 공격자에게 유용하기 때문에 제품화된(production) 환경에서는 False 로 설정해야 합니다. 하지만, 지금은 True로 설정합니다.

### url맵퍼 연결
```
# 카탈로그 애플리케이션에서 경로를 추가하려면 include()를 사용하세요.
from django.conf.urls import include
from django.urls import path

# 카탈로그 url 맵퍼
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# 기본 URL을 애플리케이션으로 리디렉션하기 위한 URL 맵 추가
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# 정적 파일(html ,css, javascript)를 제공하는것을 가능하게 하는 코드
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

- catalog 폴더에 urls.py 생성 후 아래 코드 붙여넣기

```
from django.urls import path
from catalog import views

urlpatterns = [

]
```
### 데이터 마이그레이션
```
python3 manage.py makemigrations # 모든 어플에 대한 마이그레이션 생성 ,적용X
python3 manage.py migrate # 마이그레이션 적용
```
### 웹사이트 실행
```
python3 manage.py runserver # 에러가 뜸, catalog내에 url을 정의하지 않아서
```

### 모델정의

- 필드 : 필드는 우리의 데이터베이스 목록(table)에 저장하길 원하는 데이터 열(column)을 나타냅니다.
- 레코드 : 각각의 데이터베이스 레코드(행, row)는 각 필드 값들 중 하나로 구성되어 있습니다.
    ```
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ```

- meta : 레코드 반환 순서 제어
    ```
    class Meta:
        ordering = ['-my_field_name'] # - 를 붙이면 반대로 정렬됨.

        ordering = ['title', '-pubdate'] # 알파벳 순으로 정렬 후에 발행일 별로 가장 최근 부터 정렬
    ```
- 메소드 : 기본적으로 __str__(self)메소드를 사용하여 object가 사람이 읽을수 있는 문자열을 반환합니다.
    ```
    def __str__(self):
        return self.field_name
    ```
- get_absolute_url(self) : 웹사이트의 개별적인 모델 레코드들을 보여주기 위한 URL을 반환하는 메소드입니다.
    ```
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    ```
### 모델 관리
- 모델 클래스들을 정의한 이후엔 클래스들을 사용해서 레코드들을 생성, 업데이트, 또는 삭제할 수 있고, 모든 레코드 또는 레코드의 특정 하위 집합을 가져오기 위해 쿼리를 실행할 수 있습니다.

- 레코드 생성, 수정
    ```
    # 생성
    record = MyModelName(my_field_name="Instance #1")

    # 저장
    record.save()

    # Python 속성을 사용하여 모델 필드 값에 접근
    print(record.id) # should return 1 for the first record.
    print(record.my_field_name) # should print 'Instance #1'

    # 필드를 수정한 다음 save()를 호출하여 레코드를 변경합니다.
    record.my_field_name = "New Instance Name"
    record.save()
    ```
- 레코드 가져오기
    ```
    all_books = Book.objects.all()

    # 필터 적용
    wild_books = Book.objects.filter(title__contains='wild')

    number_wild_books = Book.objects.filter(title__contains='wild').count()

    # 일대다 관계를 다른 모델에 정의하는 필드를 필터링해야 할 때, 이중 밑줄을 사용하여 관련 모델 안의 필드에 "색인(index)"할 수 있습니다.
    books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')
    ```

### 지역도서관 모델 정의하기
- models.py에 정의
#### 장르모델
```
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

def __str__(self):
    return self.name
```
#### 책 모델
```
from django.urls import reverse # URL 패턴을 뒤집어서 URL을 생성하는 데 사용됩니다.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    # 책에는 저자가 한 명만 있을 수 있지만 저자는 여러 권의 책을 가질 수 있으므로 외래 키가 사용됩니다.
    # 아직 파일에 선언되지 않았기 때문에 객체가 아닌 문자열로 작성합니다.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # 장르에 많은 책이 포함될 수 있으므로 ManyToManyField가 사용됩니다. 책은 다양한 장르를 다룰 수 있습니다.
    # 장르 클래스는 이미 정의되어 있으므로 위에서 개체를 지정할 수 있습니다.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """Model 객체를 표현하기 위한 문자열입니다."""
        return self.title

    def get_absolute_url(self):
        """이 책의 세부 기록에 액세스할 수 있는 URL을 반환합니다."""
        return reverse('book-detail', args=[str(self.id)])
```

#### 책 인스턴스 모델
- 누군가 빌릴지도 모를 특정한 책의 복사본을 나타냅니다. 그리고 복사본이 사용 가능한지 여부, 언제 되돌려받을 수 있을지, "출판사(imprint)" 또는 버전 세부 사항, 그리고 도서관 안에 있는 책의 고유 id에 대한 정보를 포함합니다.
- UUIDField 는 id 필드가 이 모델의 primary_key 로 설정되는 데 사용됩니다.
- DateField 는 due_back (만기일) 날짜에 사용됩니다.
- status 는 선택/선택 목록(choice/selection list)을 정의하는 CharField 입니다
    ```
    import uuid # Required for unique book instances

    class BookInstance(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
        book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
        imprint = models.CharField(max_length=200)
        due_back = models.DateField(null=True, blank=True)

        LOAN_STATUS = (
            ('m', 'Maintenance'),
            ('o', 'On loan'),
            ('a', 'Available'),
            ('r', 'Reserved'),
        )

        status = models.CharField(
            max_length=1,
            choices=LOAN_STATUS,
            blank=True,
            default='m',
            help_text='Book availability',
        )

        class Meta:
            ordering = ['due_back']

        def __str__(self):
            return f'{self.id} ({self.book.title})'

    ```
### 저자 모델
```
class Author(models.Model):
first_name = models.CharField(max_length=100)
last_name = models.CharField(max_length=100)
date_of_birth = models.DateField(null=True, blank=True)
date_of_death = models.DateField('Died', null=True, blank=True)

class Meta:
    ordering = ['last_name', 'first_name']

def get_absolute_url(self):
    """특정 작성자 인스턴스에 액세스하기 위한 URL을 반환합니다."""
    return reverse('author-detail', args=[str(self.id)])

def __str__(self):
    return f'{self.last_name}, {self.first_name}'
```

#### 언어모델
```
class Language(models.Model):
    """언어(예: 영어, 프랑스어, 일본어 등)를 나타내는 모델"""
    name = models.CharField(max_length=200,
                            unique=True,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def get_absolute_url(self):
        """특정 언어 인스턴스에 액세스하기 위한 URL을 반환합니다."""
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        """Model 객체를 표현하기 위한 문자열(관리 사이트 등에서)"""
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]
```

### 데이터 마이그레이션 재실행
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### 모델 등록하기
- catalog/admin.py파일
    ```
    from catalog.models import Author, Genre, Book, BookInstance

    admin.site.register(Book)
    admin.site.register(Author)
    admin.site.register(Genre)
    admin.site.register(BookInstance)
    ```

###  SuperUser 만들기
- 관리자 사이트에 로그인하기 위해서는, 직원(Staff) 상태가 활성화 된 사용자 계정이 있어야 합니다.
    ```
    # username, 이메일 주소, 그리고 강력한 비밀번호를 입력
    python3 manage.py createsuperuser
    ```
### 서버 시작해서 확인하기
-  http://127.0.0.1:8000/admin 열기
    ```
    python3 manage.py runserver
    ```

### 책추가하기
- 관리자 페이지에서 책추가하여 목록 만들기
- 대여(On loan), 사용가능(Available) 지정하기

### ModelAdmin 클래스 등록하기
- catalog/admin.py파일
- 관리자 인터페이스에서 모델이 보여지는 방식을 바꾸고 싶다면 ModelAdmin 클래스(레이아웃을 나타내는)를 정의한 후 모델 안에 등록합니다.
- 목록 뷰(List views)
    - 각각의 레코드에 표시되는 추가적인 필드/정보를 추가하기.
    - 날짜나 다른 선택 값(예: 책의 대여 상태)에 기초해서 어떤 레코드들이 목록지어질 지 선택하는 필터들 추가하기.
    - 목록 뷰(list views) 안의 동작 메뉴(actions menu)에 추가적인 옵션을 추가하고 이 메뉴가 양식 위의 어디에 보여져야 할 지 선택하기.
- 세부 뷰(Detail views)
    - 표시할(혹은 제외할)필드, 따를 순서, 그루핑, 편집 가능할지 여부, 사용될 위젯, 방향(orientation) 등등을 선택하기.
    - 인라인 편집(inline editing)기능을 넣기 위해 관련된 필드들을 레코드에 추가하기(예: 책 레코드의 저자 레코드를 생성하는 동안 책 레코드를 추가하고 편집할 수 있는 기능을 추가하기).
- fields 속성은 양식에 보여져야 할 필드들만을 순서대로 목록짓습니다. 필드들은 기본적으로 수직적으로 표시되지만, 추가적으로 그것들을 튜플 안에 그룹짓는다면 수평적으로 표시됩니다(위의 "date" 필드처럼요).
    ```
    class AuthorAdmin(admin.ModelAdmin):
        list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
        fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


    # 연관된 모델에 admin 클래스를 등록합니다.
    admin.site.register(Author, AuthorAdmin)

    # 연관된 레코드 인라인 편집 방법
    class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

    # 데코레이터를 사용하여 Book에 대한 관리 클래스를 등록합니다.
    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'display_genre')
        inlines = [BooksInstanceInline]

    # 데코레이터를 사용하여 BookInstance에 대한 관리 클래스를 등록합니다.
    @admin.register(BookInstance)
    class BookInstanceAdmin(admin.ModelAdmin):
        list_filter = ('status', 'due_back')
        fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    ```
### models.py에 Book모델 안에 추가할것
- models.py 의 book모델 안에 추가
- 불행하게도 genre 필드는 ManyToManyField이기 때문에 list_display에 직접적으로 특정할 수 없습니다.(거대한 데이터베이스 접근 "비용"이 발생할 수 있기 때문에 장고는 이것을 방지합니다). 대신 정보를 문자열로 받기 위해서 display_genre 함수를 정의할 겁니다(이것이 위에서 호출한 함수입니다; 아래에서 함수를 정의하겠습니다).
    ```
    def display_genre(self):
        """장르에 대한 문자열을 생성합니다. 이는 관리자에서 장르를 표시하는 데 필요합니다."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
    ```
### index페이지 만들기
#### url매핑
    ```
    # catalog/urls.py
    urlpatterns = [
    path('', views.index, name='index'),
    ]
    ```
#### (catalog/views.py)
    ```
    from django.shortcuts import render

    # Create your views here.

    from catalog.models import Book, Author, BookInstance, Genre # 사용할 모델 클래스

    def index(request):
        """사이트의 홈 페이지에 대한 보기 기능입니다."""

        # 일부 주요 객체의 개수 생성
        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()

        # 이용 가능한 도서 (status = 'a')
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()

        # 기본적으로 'all()'이 암시됩니다.
        num_authors = Author.objects.count()

        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
        }

        # 컨텍스트 변수의 데이터로 HTML 템플릿 index.html을 렌더링합니다.
        return render(request, 'index.html', context=context)
    ```
#### 탬플릿(locallibrary/catalog/templates/base_generic.html)
    ```
    <!doctype html>
    <html lang="en">
    <head>
    {% block title %}<title>Local Library</title>{% endblock %}
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <!-- Add additional CSS in static file -->
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    </head>
    <body>
    <div class="container-fluid">
        <div class="row">
        <div class="col-sm-2">
        {% block sidebar %}
            <ul class="sidebar-nav">
            <li><a href="{% url 'index' %}">Home</a></li>
            <li><a href="">All books</a></li>
            <li><a href="">All authors</a></li>
            </ul>
        {% endblock %}
        </div>
        <div class="col-sm-10 ">{% block content %}{% endblock %}</div>
        </div>
    </div>
    </body>
    </html>
    ```
#### CSS(locallibrary/catalog/static/css/)
    ```
    .sidebar-nav {
    margin-top: 20px;
    padding: 0;
    list-style: none;
    }
    ```
#### 사이드바(/locallibrary/catalog/templates/index.html)
    ```
    {% extends "base_generic.html" %}

    {% block content %}
    <h1>Local Library Home</h1>
    <p>Welcome to LocalLibrary, a website developed by <em>Mozilla Developer Network</em>!</p>
    <h2>Dynamic content</h2>
    <p>The library has the following record counts:</p>
    <ul>
        <li><strong>Books:</strong> {{ num_books }}</li>
        <li><strong>Copies:</strong> {{ num_instances }}</li>
        <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
        <li><strong>Authors:</strong> {{ num_authors }}</li>
    </ul>
    {% endblock %}
    ```
#### templates 경로설정
    ```
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
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

### 책목록 페이지 만들기
#### url매핑 (catalog/urls.py)
```
urlpatterns = [
path('', views.index, name='index'),
path('books/', views.BookListView.as_view(), name='books'),
]
```
#### 클래스 기반 뷰(catalog/views.py)
```
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    # 템플릿에서 사용할 변수명을 지정할 수 있음.(지정하지 않으면 modelname_list 또는 object_list)
    context_object_name = 'my_book_list'
    # 템플릿 에서 사용할 데이터를 지정할 수 있음(지정하지 않으면 전부 사용가능)
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # 템플릿 이름을 명시 할 수 있음.(명시하지 않으면 자동 서칭)
    # template_name = 'books/my_arbitrary_template_name_list.html'
```
#### 리스트뷰 템플릿 생성하기(/locallibrary/catalog/templates/catalog/book_list.html )
- modelname_list 또는 object_list라는 변수를 사용해 데이터에 접근할 수 있음.
```
{% extends "base_generic.html" %}

{% block content %}
<h1>Book List</h1>
{% if book_list %}
<ul>
    {% for book in book_list %}
    <li>
        <a href="{{ book.get_absolute_url }}">{{ book.title }}</a> ({{book.author}})
    </li>
    {% endfor %}
</ul>
{% else %}
    <p>There are no books in the library.</p>
{% endif %}
{% endblock %}

```
#### 베이스 템플릿 업데이트 (/locallibrary/catalog/templates/base_generic.html)
```
<li><a href="{% url 'index' %}">Home</a></li>
<li><a href="{% url 'books' %}">All books</a></li>
<li><a href="">All authors</a></li>
```
### Book 상세 페이지
#### url매핑 (/catalog/urls.py)
```
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<uuid:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
```
#### 클래스 기반 뷰(catalog/views.py)
```
class BookDetailView(generic.DetailView):
model = Book
```
#### 템플릿(/locallibrary/catalog/templates/catalog/book_detail.html )
- book.bookinstance_set.all : 이 메소드는 Django에 의해 자동으로 만들어진 메소드입니다. 이 메소드는 Book 과 관련된 BookInstance 레코드 집합을 반환합니다.
```
{% extends "base_generic.html" %}

{% block content %}
<h1>Title: {{ book.title }}</h1>

<p><strong>Author:</strong> <a href="">{{ book.author }}</a></p> <!-- author detail link not yet defined -->
<p><strong>Summary:</strong> {{ book.summary }}</p>
<p><strong>ISBN:</strong> {{ book.isbn }}</p>
<p><strong>Language:</strong> {{ book.language }}</p>
<p><strong>Genre:</strong> {% for genre in book.genre.all %} {{ genre }}{% if not forloop.last %}, {% endif %}{% endfor %}</p>

<div style="margin-left:20px;margin-top:20px">
    <h4>Copies</h4>

    {% for copy in book.bookinstance_set.all %}
        <hr>
        <p class="{% if copy.status == 'a' %}text-success{% elif copy.status == 'm' %}text-danger{% else %}text-warning{% endif %}">{{ copy.get_status_display }}</p>
        {% if copy.status != 'a' %}
            <p><strong>Due to be returned:</strong> {{copy.due_back}}</p>
        {% endif %}
        <p><strong>Imprint:</strong> {{copy.imprint}}</p>
        <p class="text-muted"><strong>Id:</strong> {{copy.id}}</p>
        {% endfor %}
    </div>
    {% endblock %}
```
#### 페이지네이션 적용하기
```
class BookListView(generic.ListView):
model = Book
paginate_by = 10

```
#### 모든 listview에 페이지네이션 적용하기(locallibrary/catalog/templates/base_generic.html)
```
{% block content %}{% endblock %}
{% block pagination %}
    {% if is_paginated %}
        <div class="pagination">
        <span class="page-links">
            {% if page_obj.has_previous %}
            <a href="{{ request.path }}?page={{ page_obj.previous_page_number }}">previous</a>
            {% endif %}
            <span class="page-current">
            <p>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.</p>
            </span>
            {% if page_obj.has_next %}
            <a href="{{ request.path }}?page={{ page_obj.next_page_number }}">next</a>
            {% endif %}
        </span>
        </div>
    {% endif %}
{% endblock %}
```

### 세션이란?
- 사이트와 특정 브라우저 사이의 "state"를 유지시키는 것입니다. 세션은 당신이 매 브라우저마다 임의의 데이터를 저장하게 하고, 이 데이터가 브라우저에 접속할 때 마다 사이트에서 활용될 수 있도록 합니다.
- settings.py (세션 사용설정)
```
INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ....
```

### 지역도서관 세션 만들기 (방문자 수 받아오기)
#### 뷰 수정 (/locallibrary/catalog/views.py)
```
def index(request):
...

num_authors = Author.objects.count()  # The 'all()' is implied by default.

# Number of visits to this view, as counted in the session variable.
num_visits = request.session.get('num_visits', 0)
request.session['num_visits'] = num_visits + 1

context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_visits': num_visits,
}

# Render the HTML template index.html with the data in the context variable.
return render(request, 'index.html', context=context)

```
#### 템플릿 수정 (/locallibrary/catalog/templates/index.html)
```
<h2>Dynamic content</h2>

<p>The library has the following record counts:</p>
<ul>
    <li><strong>Books:</strong> {{ num_books }}</li>
    <li><strong>Copies:</strong> {{ num_instances }}</li>
    <li><strong>Copies available:</strong> {{ num_instances_available }}</li>
    <li><strong>Authors:</strong> {{ num_authors }}</li>
</ul>

<p>
    You have visited this page {{ num_visits }}{% if num_visits == 1 %} time{% else %} times{% endif %}.
</p>

```
### 사용자 인증 및 권한
- 인증 활성화 (settings.py)
```
INSTALLED_APPS = [
    # …
    'django.contrib.auth',  # Core authentication framework and its default models.
    'django.contrib.contenttypes',  # Django content type system (allows permissions to be associated with models).
    # …

MIDDLEWARE = [
    # …
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages sessions across requests
    # …
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests using sessions.
    # …

```
- admin페이지 에서 그룹 및 유저 등록 (사진으로 설명되있어서 생략)
#### url추가 (locallibrary/urls.py)
```
# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
```
#### templates 폴더 아래에 registration 폴더 추가
- settings.py
```
import os # needed by code below
    # …
TEMPLATES = [
    {
    # …
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    # …
```
#### 로그인 페이지(/templates/registration/login.html)
```
{% extends "base_generic.html" %}

{% block content %}

{% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
{% endif %}

{% if next %}
    {% if user.is_authenticated %}
    <p>Your account doesn't have access to this page. To proceed,
    please login with an account that has access.</p>
    {% else %}
    <p>Please login to see this page.</p>
    {% endif %}
{% endif %}

<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
    <tr>
        <td>{{ form.username.label_tag }}</td>
        <td>{{ form.username }}</td>
    </tr>
    <tr>
        <td>{{ form.password.label_tag }}</td>
        <td>{{ form.password }}</td>
    </tr>
    </table>
    <input type="submit" value="login">
    <input type="hidden" name="next" value="{{ next }}">
</form>

{# Assumes you set up the password_reset view in your URLconf #}
<p><a href="{% url 'password_reset' %}">Lost password?</a></p>

{% endblock %}

```
#### 로그인 후 이동할 페이지 설정 (settings.py)
```
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
```
#### 로그아웃 페이지 생성(templates/registration/logged_out.html)
```
{% extends "base_generic.html" %}

{% block content %}
<p>Logged out!</p>
<a href="{% url 'login'%}">Click here to login again.</a>
{% endblock %}
```
#### 비밀번호 재설정 페이지(templates/registration/password_reset_form.html)
```
{% extends "base_generic.html" %}

{% block content %}
<form action="" method="post">
{% csrf_token %}
{% if form.email.errors %}
    {{ form.email.errors }}
{% endif %}
    <p>{{ form.email }}</p>
    <input type="submit" class="btn btn-default btn-lg" value="Reset password">
</form>
{% endblock %}

```
#### 비밀번호 재설정 완료 페이지(/templates/registration/password_reset_done.html)
```
{% extends "base_generic.html" %}

{% block content %}
<p>We've emailed you instructions for setting your password. If they haven't arrived in a few minutes, check your spam folder.</p>
{% endblock %}
```
#### 비밀번호 재설정 이메일 페이지(templates/registration/password_reset_email.html )
```
Someone asked for password reset for email {{ email }}. Follow the link below:
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
```
#### 비밀번호 재설정 확인 페이지(templates/registration/password_reset_confirm.html )
```
{% extends "base_generic.html" %}

{% block content %}
    {% if validlink %}
        <p>Please enter (and confirm) your new password.</p>
        <form action="" method="post">
        {% csrf_token %}
            <table>
                <tr>
                    <td>{{ form.new_password1.errors }}
                        <label for="id_new_password1">New password:</label></td>
                    <td>{{ form.new_password1 }}</td>
                </tr>
                <tr>
                    <td>{{ form.new_password2.errors }}
                        <label for="id_new_password2">Confirm password:</label></td>
                    <td>{{ form.new_password2 }}</td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Change my password"></td>
                </tr>
            </table>
        </form>
    {% else %}
        <h1>Password reset failed</h1>
        <p>The password reset link was invalid, possibly because it has already been used. Please request a new password reset.</p>
    {% endif %}
{% endblock %}
```
#### 비밀번호 재설정 완료 페이지(templates/registration/password_reset_complete.html)
```
{% extends "base_generic.html" %}

{% block content %}
<h1>The password has been changed!</h1>
<p><a href="{% url 'login' %}">log in again?</a></p>
{% endblock %}
```
#### 사이드바 넣기(catalog/templates/base_generic.html)
```
    <ul class="sidebar-nav">
    …
{% if user.is_authenticated %}
    <li>User: {{ user.get_username }}</li>
    <li>
    <form id="logout-form" method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-link">Logout</button>
    </form>
    </li>
{% else %}
    <li><a href="{% url 'login' %}?next={{ request.path }}">Login</a></li>
{% endif %}
    …
</ul>

```
#### 사이드바 배치 수정(catalog/static/css/styles.css)
```
#logout-form {
display: inline;
}
#logout-form button {
padding: 0;
margin: 0;
}
```

### 사용자별 뷰 제한하기
#### (Catalog/models.py)
```
from django.conf import settings

borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

# 책 인스턴스의 기한이 지났는지 알려주기 위해 템플릿에서 호출할 수 있는 속성
from datetime import date

@property
def is_overdue(self):
    """Determines if the book is overdue based on due date and current date."""
    return bool(self.due_back and date.today() > self.due_back)
```
#### 마이그레이션 하기
#### (Catalog/admin.py)
```
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
```
#### 관리자로 로그인해서 사용자 도서 대출하기
### 대출한 책 보는 페이지 제작
#### 대출한 책 보는 페이지 url 추가(/catalog/urls.py)
```
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
```
#### 대출한 책 보기(Catalog/views.py)
```
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )
```
#### 템플릿 만들기(templates/catalog/bookinstance_list_borrowed_user.html )
```
{% extends "base_generic.html" %}

{% block content %}
    <h1>Borrowed books</h1>

    {% if bookinstance_list %}
    <ul>

    {% for bookinst in bookinstance_list %}
    <li class="{% if bookinst.is_overdue %}text-danger{% endif %}">
        <a href="{% url 'book-detail' bookinst.book.pk %}">{{ bookinst.book.title }}</a> ({{ bookinst.due_back }})
    </li>
    {% endfor %}
    </ul>

    {% else %}
    <p>There are no books borrowed.</p>
    {% endif %}
{% endblock %}
```
- http://127.0.0.1:8000/catalog/mybooks/ 에서 확인

#### 사이드바에 "My Borrowed" 줄을 추가(templates/base_generic.html)
```
<ul class="sidebar-nav">
{% if user.is_authenticated %}
<li>User: {{ user.get_username }}</li>

<li><a href="{% url 'my-borrowed' %}">My Borrowed</a></li>

<li>
    <form id="logout-form" method="post" action="{% url 'admin:logout' %}">
    {% csrf_token %}
    <button type="submit" class="btn btn-link">Logout</button>
    </form>
</li>
{% else %}
<li><a href="{% url 'login' %}?next={{ request.path }}">Login</a></li>
{% endif %}
</ul>
```
#### 권한 추가하기
```
class BookInstance(models.Model):
# …
class Meta:
    # …
    permissions = (("can_mark_returned", "Set book as returned"),)
```

### 과제 (스태프로 모든 대출 목록 확인하기)
#### url
```
urlpatterns += [
    path('allbooks/', views.AllLoanedBooksByUserListView.as_view(), name='all-borrowed'),
]
```
#### view
```
# 모든 대출목록 확인
class AllLoanedBooksByUserListView(generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/all_bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(status__exact='o')
            .order_by('due_back')
        )
```
#### 템플릿
```
{% extends "base_generic.html" %}

{% block content %}
    <h1>All Borrowed books</h1>

    {% if bookinstance_list %}
    <ul>

    {% for bookinst in bookinstance_list %}
    <li class="{% if bookinst.is_overdue %}text-danger{% endif %}">
        <a href="{% url 'book-detail' bookinst.book.pk %}">{{ bookinst.book.title }}</a> ({{ bookinst.due_back }})
    </li>
    {% endfor %}
    </ul>

    {% else %}
    <p>There are no books borrowed.</p>
    {% endif %}
{% endblock %}
```
#### 사이드바
```
<li><a href="{% url 'all-borrowed' %}">All Borrowed</a></li>
```

### form 생성하고 데이터 유효성 검사하기
#### form 필드
- required: True 로 설정되면, 필드를 빈칸으로 두거나 None 값을 줄 수 없게된다. 보통필드는 required는 True로 기본 설정되므로, 폼에서 빈 칸을 허용하기 위해서는required=False 로 설정해야 한다.
-label: HTML에서 필드를 렌더링할때 사용하는 레이블이다. label 이 지정되지 않으면, Django는 필드 이름에서 첫번째 문자를 대문자로, 밑줄을 공백으로 변형한 레이블을 새로 생성할 것이다. (예를 들면, renewaldate --> _Renewal date).
- label_suffix: 기본적으로, 콜론(:)이 레이블 다음에 표시된다. (예를 들면, Renewal date**:**). 이 인자는 다른 문자(들)를 포함한 접미사를 지정할 수 있도록 해준다.
- initial: 폼이 나타날 때 해당 필드의 초기 값.
- widget: 사용할 디스플레이 위젯.
- help_text (위의 예에서 봤듯이): 필드 사용법을 보여주는 추가적인 문구.
- error_messages: 해당 필드의 에러 메시지 목록. 필요하면 문구를 수정할 수 있다.
- validators: 해당 필드가 유효한 값을 가질 때 호출되는 함수의 목록.
- localize: 폼 데이타 입력의 현지화(localisation)를 허용함 (자세한 정보는 해당 링크 참조).
- disabled: 이 옵션이 True 일때 해당 필드를 볼 수는 있지만 편집이 안됨. 기본 값은 False.

#### form 생성(locallibrary/catalog/forms.py)
```
from django import forms

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

```
#### form업데이트(유효성 체크)
```
import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

```
#### URL Configuration 작성하기(locallibrary/catalog/urls.py)
```
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
```
#### 뷰 만들기
```
import datetime

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm

def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # POST 요청이면 폼 데이터를 처리한다
    if request.method == 'POST':

        # 폼 인스턴스를 생성하고 요청에 의한 데이타로 채운다 (binding):
        book_renewal_form = RenewBookForm(request.POST)

        # 폼이 유효한지 체크한다:
        if book_renewal_form.is_valid():
            # form.cleaned_data 데이타를 요청받은대로 처리한다(여기선 그냥 모델 due_back 필드에 써넣는다)
            book_instance.due_back = book_renewal_form.cleaned_data['renewal_date']
            book_instance.save()

            # 새로운 URL로 보낸다:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # GET 요청 (혹은 다른 메소드)이면 기본 폼을 생성한다.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        book_renewal_form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': book_renewal_form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)

```
- get_object_or_404(): 해당 모델의 기본 키(primary key) 값에 연결되는 특정 객체를 반환하거나 해당 record가 없을경우 Http404예외를 발생시킨다.
- HttpResponseRedirect: 특정 URL로의 재전송을 생성한다. (HTTP status code 302).
- reverse(): URL 설정(configuration) 의 이름과 전달인자들로 부터 URL을 만들어낸다. 템플릿에서 사용했던 url태그에 해당하는 파이썬 형식의 동일 표현이다.
- datetime: 날짜와 시간을 다루는 파이썬 라이브러리 이다.
#### 사용권한설정(locallibrary/catalog/views.py )
```
import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """도서관 사서에 의해 특정 BookInstance를 갱신하는 뷰 함수."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # POST 요청이면 폼 데이터를 처리한다
    if request.method == 'POST':

        # 폼 인스턴스를 생성하고 요청에 의한 데이타로 채운다 (binding):
        book_renewal_form = RenewBookForm(request.POST)

        # 폼이 유효한지 체크한다:
        if book_renewal_form.is_valid():
            # book_renewal_form.cleaned_data 데이타를 요청받은대로 처리한다(여기선 그냥 모델 due_back 필드에 써넣는다)
            book_instance.due_back = book_renewal_form.cleaned_data['renewal_date']
            book_instance.save()

            # 새로운 URL로 보낸다:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # GET 요청(혹은 다른 메소드)이면 기본 폼을 생성한다.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        book_renewal_form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': book_renewal_form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)
```

#### 템플릿(catalog/templates/catalog/book_renew_librarian.html)
```
{% extends "base_generic.html" %}

{% block content %}
  <h1>Renew: {{ book_instance.book.title }}</h1>
  <p>Borrower: {{ book_instance.borrower }}</p>
  <p> if book_instance.is_overdue %} class="text-danger"{% endif %}>Due date: {{book_instance.due_back}}</p>

  <form action="" method="post">
    {% csrf_token %}
    {{ form.as_table }}
    <input type="submit" value="Submit">
  </form>
{% endblock %}
```
###
#### urls(locallibrary/catalog/urls.py)
```
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
```
#### views.py 아래추가
```
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'05/01/2018',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

```
#### 템플릿(locallibrary/catalog/templates/catalog/author_form.html)
```
{% extends "base_generic.html" %}

{% block content %}
  <form action="" method="post">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
    </table>
    <input type="submit" value="Submit" />
  </form>
{% endblock %}
```
#### 삭제(locallibrary/catalog/templates/catalog/author_confirm_delete.html)
```
{% extends "base_generic.html" %}

{% block content %}
  <h1>Delete Author</h1>

  <p>Are you sure you want to delete the author: {{ author }}?</p>

  <form action="" method="POST">
    {% csrf_token %}
    <input type="submit" action="" value="Yes, delete." />
  </form>
{% endblock %}
```
### 과제 책 등록, 수정, 삭제 페이지 만들기


### 테스트 자동화
#### catalog/tests폴더 생성
- test_models.py
- test_views.py
- test_forms.py

#### test_models.py
```
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
```
#### 테스트 실행
```
# test*로 시작하는 모든 파일 체크 --> 근데 하위 폴더 탐색 안함 ㅡㅡ;
python3 manage.py test

# ValueError: Missing staticfiles manifest entry ...에러 나면
python3 manage.py collectstatic

# 부분실행 catalog/tests 아래 파일만 체크
python3 manage.py test catalog/tests

# 설명 레벨 설정 0,1,2,3
python3 manage.py test --verbosity 2
```

### 배포

#### settings.py
```
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag'
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

```
#### 체크리스트 확인
```
python3 manage.py check --deploy
```

#### Heroku 프리티어 사용


#### 깃에 어플 등록하기

#### HTTP서버 설치
```
pip3 install gunicorn
```

#### 데이터 베이스 설정
- 환경변수 자동 설정
```
# 환경변수 자동 설정
pip3 install dj-database-url
```
- settings.py 설정 (맨 아래 추가)
```
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```
- PSYCOPG2 (PYTHON POSTGRES 데이터베이스 지원용) 설치하기
```
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
pip3 install psycopg2
```
- SETTINGS.PY 수정하기 (맨 아래)
```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'
```
#### WHITENOISE 설치하기
```
pip3 install whitenoise
```
- SETTINGS.PY 수정하기 (미들웨어에)
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 정적 파일 크기 줄이기
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
#### 관련 라이브러리 설치
- requirements.txt 에 라이브러리 입력
```
dj-database-url==0.4.1
Django==2.0
gunicorn==19.6.0
psycopg2==2.6.2
whitenoise==3.2.2
```
- 설치
```
pip3 freeze > requirements.txt
```

- runtime.txt (프로그래밍 언어 설정)
```
python-3.6.4
```
#### 모든 변경사항 github에 저장하기

#### 로컬에서 마지막 테스트 하기
- python3 manage.py runserver


#### heroku 계정 생성하기
- www.heroku.com 사이트로 가서 SIGN UP FOR FREE 버튼을 클릭한다.
- 세부 정보를 입력하고 CREATE FREE ACCOUNT 버튼을 누른다. 당신은 가입 이메일에서 계정을 확인 하도록 요청받을 것이다.
- 가입 이메일에서 계정 활성화 요청 링크 (account activation link) 를 클릭하면 웹 브라우저 상에서 당신의 계정 위치로 이동될 것이다.
- 당신의 암호를 입력하고 SET PASSWORD AND LOGIN 버튼을 클릭하라
- 로그인이 되면 Heroku 대시보드로 이동될 것이다: https://dashboard.heroku.com/apps.
#### Heroku 클라이언트 설치하기
#### 웹사이트를 생성하고 업로드하기
- heroku create

#### Heroku저장소에 등록하기
```
git push heroku master
```

#### 마이그레이트
```
heroku run python manage.py migrate
```

#### 관리자 아이디 생성
```
heroku run python manage.py createsuperuser
```

#### 브라우저로 확인
```
heroku open
```
#### 애드온 관리하기
- heroku addons 명령으로 앱의 애드온 적용에 대해 확인할 수 있다. 이 명령은 모든 애드온을 나열하고, 가격과 상태를 보여준다.
```
heroku addons
#자세히
heroku addons:open heroku-postgresql

# 구성변수 설정
heroku config

# setcret키, 디버그 설정
heroku config:set
DJANGO_SECRET_KEY=eu09(ilk6@4sfdofb=b_2ht@vad*$ehh9-)3u_83+y%(+phh&=
heroku config:set DJANGO_DEBUG=
```

#### settings.py (배포 url 추가)
```
ALLOWED_HOSTS = ['<your app URL without the https:// prefix>.herokuapp.com','127.0.0.1']
# For example:
# ALLOWED_HOSTS = ['fathomless-scrubland-30645.herokuapp.com','127.0.0.1']
```

#### 깃허브에 반영
```
git add -A
git commit -m 'Update ALLOWED_HOSTS with site and development server URL'
git push origin master
git push heroku master
```
