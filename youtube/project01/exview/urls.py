from django.urls import path
from . import views

app_name = 'exview'

urlpatterns = [
    path('', views.index, name='index'),
    # 함수형 뷰
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

    # 클래스형 뷰
    # get요청
    path('get3/', views.ExamGet3.as_view(), name = 'get3'),
    path('get4/<int:n1>/<int:n2>/<str:n3>/', views.ExamGet4.as_view(), name='get4'),
    # post 요청
    path('post3/', views.ExamPost3.as_view(), name = 'post3'),
    path('post4/<str:msg>/<int:n>/', views.ExamPost4.as_view(), name = 'post4'),

    # getpost요청
    path('getpost2/', views.ExamGetPost2.as_view(), name = 'getpost2')
]
