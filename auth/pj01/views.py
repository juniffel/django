from django.shortcuts import render,redirect
from. import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,logout,login

def index(request):
  if request.user: # 로그아웃
    del request.user
  # print(request.user)

  # POST 요청으로 로그인 시도
  if request.method =='POST':
    print('post요청입니다.')
    # print(f'POST요청 : {request.__dict__}')

    id = request.POST['username']
    pwd = request.POST['password']

    # 유효성 검사
    if len(id)>20:
      print(f'username이 20자를 넘었습니다.')
    if len(pwd)>200:
      print(f'password가 200자를 넘었습니다.')

    user = models.User.objects.get(username=id)
    # 로그인 인증
    # print(f'인증 절차 : user:{user.username}\nuser의 password:{user.password}\n로그인한 사용자의 password:{pwd}')
    if check_password(pwd, user.password):
      # print(f'로그인한 사용자의 비밀번호:{pwd},{user.username}의 비밀번호:{user.password}가 일치하므로 인증에 성공하였습니다.')
      login(request, user)
      return render(request,'pj01/home.html',{'user':user})
    else:
      # print(f'인증 실패')
      return redirect('pj01:index')
  # get요청으로 화면 로드할 때
  print('get요청입니다.')
  return render(request,'pj01/index.html')

def signup(request):
  model = models.User
  if request.method == 'POST':
    id = request.POST['username']
    pwd1 = request.POST['password1']
    pwd2 = request.POST['password2']

    # 유효성 검사
    if id and pwd1 and pwd2 and pwd1==pwd2:

      #쿼리 저장
      user = model(username = id, password = pwd1)
      user.save()
      username= model.objects.get(username=id).username
      # print(username.username)
      return render(request, 'pj01/home.html', {'username':username})
  return render(request, 'pj01/signup.html')
