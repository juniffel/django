from django.urls import path

from . import views
app_name = 'pj01'

urlpatterns = [
  path('',views.index, name='index'),
  path('home',views.index, name='home'),
  path('signup',views.signup, name='signup'),
]
