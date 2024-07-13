from django.shortcuts import render
from django.utils import timezone
# Create your views here.
def index(request):
    print(request.COOKIES)
    print(request.session)
    print(request.session.session_key)
    request.session['now'] = '2024-07-13'
    return render(request, 'ex_cookie/index.html',{'cookies':request.COOKIES})

from django.http import HttpResponse

def session_cookie(request):
    print('로그인 상태:', request.session.get('login_user'))
    response = HttpResponse('세션 쿠키 생성')
    if not request.COOKIES.get('mycookie'):
        cname = 'mycookie'
        cval = timezone.now()
        response.set_cookie(cname,cval) # 세션 쿠키
    return response


def permanent_cookie(request):
    print('로그인 상태:', request.session.get('login_user'))

    response = HttpResponse('영구(permanent) 쿠키 생성')

    if not request.COOKIES.get('mycookie2'):
        cname = 'mycookie2'
        cval = timezone.now().day
        response.set_cookie(
            cname,
            cval,
            max_age = 60) # 영구쿠키는 max_age로 활성시간 설정
    return response

def login(request):
    if request.method == 'GET':
        remember_id = request.COOKIES.get('id','')
        return render(request, 'ex_cookie/login.html',{'remember_id':remember_id})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        remember = request.POST.get('remember', '')
        response = HttpResponse('로그인 성겅')
        if id ==pw:
            request.session['login_user'] = id
            if remember == '':
                response.delete_cookie('id')
            else:
                response.set_cookie('id',id,max_age=60)
            return response
        else:
            return render(request, 'ex_cookie/login.html')

from django.shortcuts import redirect, reverse
def logout(request):
    request.session.flush()
    response = redirect(reverse('ex_cookie:index'))
    return response
