from django.urls import path
from . import views
app_name=  'pj02'

urlpattern= [
  path('', views.index, name = 'index'),
]
