from django.urls import path

from . import views
app_name = 'info'

urlpatterns=[
    path('', views.index.as_view(), name = 'index')
]
