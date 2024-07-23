from django.shortcuts import render

from . import models
# Create your views here.

def index(request):
    question_list = models.Question.objects.order_by('-title')
    return render(request,'board/index.html', {'question_list':question_list})
