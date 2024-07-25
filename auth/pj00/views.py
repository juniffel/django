from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import time
# Create your views here.

def index(request):
  data = User.objects.all()
  print(f'경로:{request.path}')
  template = 'log/index.html'
  # print(data)
  context = {'data' : data}
  return render(request, template, context)

def login(request):
  print(f'로그인 뷰 진입')
  # for i in request.__dict__:
  #   print(f'{i}:{request.__dict__[i]}')
  if request.method =='POST':
    print(f'POST 요청 처리')
    username = request.POST['username']
    password = request.POST['password']
    print(f"username:{request.POST['username']}")
    print(f"password:{request.POST['password']}")
    print(f'유효성 검사')
    if username and password:# 폼 클래스를 쓰지않고 직접 유효성 처리, 폼클래스를 쓰면 form.is_valid()로 처리 가능
      print('로그인 인증 처리')
      c_user = User.objects.get(username=username)
      print(f'모델에 정의된 아이디 비번 : {c_user, c_user.password}')
      if c_user.password == password: # 아이디 비밀번호 매칭확인
          request.session['user_id'] = c_user.id # 세션에 등록
          print(f'로그인 세션 확인 : {request.session["user_id"]}')
          print(f'로그인한 유저가 있는지 확인 : {request.user}')
          return redirect('log:index')
      else:
          context = {'error': '인증 실패'}
          return render(request, 'log/login.html', context)

    return render(request,'log/index.html')
  else:
    print(f'GET요청 처리')
    return render(request,'log/login.html')

def logout(request):
  # 현재 사용자 세션에서 사용자 정보를 삭제
  if request.user.is_authenticated:
      # 사용자 세션 삭제
      request.session.flush()  # 세션 초기화
      # request.user.logout() # 을 사용할 수도 있음

  # 로그아웃 후 이동할 URL
  return redirect('log:index')  # 'home'은 로그아웃 후 리다이렉트할 URL의 이름
