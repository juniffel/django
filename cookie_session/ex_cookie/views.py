
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone


def index(request):
  print(request.COOKIES)
  return render(request,'ex_cookie/index.html',{'cookies':request.COOKIES})

def session_cookie(request):
  response = HttpResponse('세션쿠키 생성')
  if not request.COOKIES.get('mycookie'):
    cname = 'mycookie'
    cval = timezone.now()
    response = render(request,'ex_cookie/index.html')
    response.set_cookie(cname,cval)# 세션쿠키
  return response

def permanent_cookie(request):
  response = HttpResponse('영구(permanent) 쿠키생성)')

  if not request.COOKIES.get('mycookie2'):
    cname = 'mycookie2'
    cval = timezone.now().day
    response.set_cookie(
    cname,
    cval,
    max_age = 60 # 초단위 60*60*24*365 와 같은 방식으로 설정
    )# 영구 쿠키
  return response


def login(request):
  if request.method=='GET':
    remember_id = request.COOKIES.get('id','')
    return render(request,'ex_cookie/login.html',{'remember_id':remember_id})

  else:
    id = request.POST['id']
    pw = request.POST['pw']
    remember = request.POST.get('remember','')
    response = HttpResponse('로그인 성공')
    if id ==pw:
      if remember=='':
        response.delete_cookie('id')
      else:
        response.set_cookie('id',id,max_age=60*60)
      return response
    else:
      return render(request,'ex_cookie/login.html')
