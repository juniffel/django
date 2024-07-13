from django.urls import path
from .import views

app_name = 'ex_form'

urlpatterns = [
    path('exam01/',views.exam01, name = 'exam01'),
    path('exam02/',views.exam02, name = 'exam02'),
    path('exam03/',views.exam03, name = 'exam03'),
    path('',views.index, name = 'index'),
    #클래스 뷰
    path('exam04/', views.Myview1.as_view(), name = 'exam04'),
    path('exam05/', views.Myview2.as_view(), name = 'exam05'),
    path('exam06/', views.Myview3.as_view(), name = 'exam06'),
    path('exam07/', views.Myview4.as_view(), name = 'exam07'),
    path('exam08/<int:pk>/', views.Myview5.as_view(), name = 'exam08'),
    path('exam09/', views.Myview6.as_view(), name = 'exam09'),
    path('exam10/<int:pk>/', views.Myview7.as_view(), name = 'exam10'),
    path('exam11/<int:pk>/', views.Myview8.as_view(), name = 'exam11'),

]
