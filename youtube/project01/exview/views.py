from django.shortcuts import render # 템플릿 사용할 때
from django.http import HttpResponse, HttpResponseRedirect # 응답을 직접만들때
from django.utils import timezone
from django.urls import reverse
# Create your views here.
def index(request):
    # print('클라이언트로 요청받음.')
    # print('=========requset 속성=========')
    # print('scheme:',request.scheme)
    # print('body:',request.body)
    # print('path:',request.path)
    # print('path_info:',request.path_info)
    # print('method:',request.method)
    # print('encoding:',request.encoding)
    # print('content_type:',request.content_type)
    # print('GET:',request.GET)
    # print('POST:',request.POST)
    # print('COOKIES:',request.COOKIES)
    # print('FILES:',request.FILES)
    # print('headers:',request.headers)
    # print('=======================')
    # print('session:', request.session)
    # print('user:', request.user)
    # print('=================Method')
    # print('get_host():', request.get_host())
    # print('get_port():', request.get_port())
    # print('get_full_path():', request.get_full_path())
    # print('get_full_path_info():', request.get_full_path_info())
    # print('build_absolute_uri():', request.build_absolute_uri())
    # print('==================응답')
    # response = HttpResponse('Hello')
    # print('content:', response.content)
    # print('headers:', response.headers)
    # print('charset:', response.charset)
    # print('status_code:', response.status_code)
    # print('items:', response.items())
    # print('======================')
    # return HttpResponse('응답데이터')
    now = timezone.now()
    print('현재 시간:', now)
    print(reverse('exview:index'))
    print(reverse('exview:get1'))
    print(reverse('exview:get2',args=(11,22,'hell')))
    return render(request, 'exview/index.html', {'now':now})

def get1(request):
    print(f'get1 요청이 들어옴')
    print(f'요청 정보 : {request.GET}')
    print(f'요청 정보에 있는 키들 : {request.GET.keys()}')
    print(f'요청 정보에 있는 값들 : {request.GET.values()}')
    return HttpResponse('get1')

def get2(request,n1,n2,n3):
    print(f'get2 요청이 들어옴')
    print(f'n1:{n1}')
    print(f'n2:{n2}')
    print(f'n3:{n3}')
    return HttpResponse('get2')

def post1(request):
    print('POST1 요청이 들어옴.')
    print(f'요청 정보 : {request.POST}')
    print(f'요청 정보에 있는 키들 : {request.POST.keys()}')
    print(f'요청 정보에 있는 값들 : {request.POST.values()}')
    return HttpResponse('post1')


def post2(request,msg,n):
    print('POST2 요청이 들어옴.')
    print(f'msg:{msg}, n:{n}')
    return HttpResponse('post2')

def getpost1(request):
    print(request.method)
    if request.method == 'GET':
        print('get요청 처리')
    elif request.method == 'POST':
        print('post요청 처리')
    return HttpResponse('getpost1')

# 클래스형 뷰
from django.views.generic import View

class ExamGet3(View):
    def get(self, request):
        print(f'get3/요청이 들어옴')
        print(f'요청 정보 : {request.GET}')
        print(f'요청 정보에 있는 키들 : {request.GET.keys()}')
        print(f'요청 정보에 있는 값들 : {request.GET.values()}')
        return HttpResponse('get3')
class ExamGet4(View):
    def get(self, request,n1,n2,n3):
        print(f'get4/요청이 들어옴')
        print(f'n1:{n1}')
        print(f'n2:{n2}')
        print(f'n3:{n3}')
        return HttpResponse('get4')

class ExamPost3(View):
    def post(self, request):
        print('POST3 요청이 들어옴.')
        print(f'요청 정보 : {request.POST}')
        print(f'요청 정보에 있는 키들 : {request.POST.keys()}')
        print(f'요청 정보에 있는 값들 : {request.POST.values()}')
        return HttpResponse('post3')
class ExamPost4(View):
    def post(self, request,msg,n):
        print('POST4 요청이 들어옴.')
        print(f'msg:{msg}, n:{n}')
        return HttpResponse('post4')

class ExamGetPost2(View):
    def get(self, request):
        print('get요청 처리')
        return HttpResponse('getpost2/(GET)')
    def post(self, request):
        print('post요청으로 처리')
        user = request.POST['user']
        pwd = request.POST['pwd']
        if user == pwd:
            print('로그인')
            return HttpResponse('getpost2/(POST)')
        else:
            print('로그인 실패')
            return HttpResponseRedirect('/exview/')
