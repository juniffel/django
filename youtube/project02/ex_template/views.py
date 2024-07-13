from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'ex_template/index.html', context)

def ex01(request):
    n1 = 100
    lst = [1,2,3]
    tup = (4,5,6)
    dict = {'a':1, 'b':2, 'c':3}
    context = {
        'n1':n1,
        'lst':lst,
        'tup':tup,
        'dict':dict,
    }
    return render(request, 'ex_template/ex01.html', context)

def ex02(request):
    val1 = 'hello<world><br>'
    lst = ['hO','Hi','weLCome']
    tup = (1,2,3)
    dict = {'aa':10,'bb':20,'cc':30}
    bio = 'hi1  hi2 hi3 hi4 hi5 hi6 hi7 hi8 hi9 hi10'
    ls = [100]
    lss = [100,200]
    data = {
        'val1':val1, 'lst':lst, 'tup':tup,
        'dict':dict, 'bio':bio, 'ls':ls, 'lss':lss,
    }
    return render(request, 'ex_template/ex02.html', data)

class Info:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Info[name={self.name},age={self.age}]'

def ex03(request):
    name_list = ['홍', '장', '이', '박']
    info_list = [
        Info('홍', 33),
        Info('장', 29),
        Info('이', 28),
        Info('박', 29),
    ]
    context = {
        'name_list':name_list,
        'info_list':info_list,
    }
    return render(request, 'ex_template/ex03.html', context)

def ex04(request):
    name_list = ['홍', '장', '이', '박']
    info_list = [
        Info('홍', 33),
        Info('장', 29),
        Info('이', 28),
        Info('박', 29),
    ]
    context = {
        'value':100,
        'name_list':name_list,
        'info_list':info_list,
    }
    return render(request, 'ex_template/ex04.html', context)

from django.urls import reverse
def ex05(request):
    url_list = [
        reverse('ex_template:index'),
        reverse('ex_template:ex01'),
        reverse('ex_template:ex02'),
        reverse('ex_template:ex03'),
        reverse('ex_template:ex04'),
    ]
    return render(request, 'ex_template/ex05.html', {'url_list':url_list})


def ex06(request):
    if request.method == 'GET':
        return render(request, 'ex_template/ex06.html')
    elif request.method =='POST':
        id = request.POST['id']
        pw = request.POST['pwd']
        if id==pw:
            return HttpResponse('로그인 성공')
        else:
            return HttpResponseRedirect(reverse('ex_template:ex06'))
def ex07(request):
    value = 100
    info = Info('홍', 33)
    context = {
        'value':value,
        'info':info,
    }
    return render(request, 'ex_template/ex07.html', context)

def ex08(request):
    html = '<h1>Hello</h1> 홍길동'
    ctx={
        'html':html
    }
    return render(request , 'ex_template/ex08.html', ctx)
def ex09(request):
    return render(request, 'ex_template/ex09.html')
