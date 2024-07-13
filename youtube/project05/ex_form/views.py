from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Person
def exam01(request):
    if request.method =='POST':
        name = request.POST['name']
        age = request.POST['age']
        print('요청처리:', name, age)
        Person(name = name, age=age).save()
        return HttpResponse('처리완료')
    else:
        return render(request, 'ex_form/exam01_form.html')

from .forms import PersonForm

def exam02(request):
    if request.method == 'POST':
        personForm = PersonForm(request.POST)
        if personForm.is_valid(): # 유효성 검증
            name = personForm.cleaned_data['name']
            age = personForm.cleaned_data['age']
            Person(name=name, age=age).save()
            return HttpResponse('처리완료')
        else:
            return render(
            request,
            'ex_form/exam02_form.html',
            {'form':personForm}
        )
    else:
        form = PersonForm()
        return render(
            request,
            'ex_form/exam02_form.html',
            {'form':form}
        )
from .forms import PersonModelForm

def exam03(request):
    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('처리완료')
    else:
        form = PersonModelForm()

    return render(
        request,
        'ex_form/exam03_form.html',
        {'form':form}
        )

def index(request):
    return render(request, 'ex_form/index.html')

from django.views.generic import View
from django.shortcuts import redirect, reverse

# 클래스 뷰
class Myview1(View):
    def get(self,request):
        form = PersonModelForm()
        return render(request, 'ex_form/exam04_form.html', {'form':form})
    def post(self, request):
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ex_form:index'))
        return render(request, 'ex_form/exam04_form.html', {'form':form})

# 클래스 뷰
class Myview2(View):
    form_class = PersonModelForm
    initial = {
        'name':'이름',
        'age':0
    }
    template_name = 'ex_form/exam04_form.html'
    def get(self,request):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ex_form:index'))
        return render(request, self.template_name, {'form':form})


# generic 뷰

from django.views.generic import FormView

class Myview3(FormView):
    form_class = PersonModelForm
    template_name = 'ex_form/exam04_form.html'
    success_url = '/ex/'

    def form_valid(self, form):
        print('데이터가 유효하면 즈어장')
        m = Person(**form.cleaned_data)
        m.save()

        return super().form_valid(form)


from django.views.generic import CreateView

class Myview4(CreateView):
    model = Person
    form_class = PersonModelForm
    # 템플릿을 지정하지않으면 모델이름_form.html을 자동으로 찾음.
    # template_name = 'ex_form/exam04_form.html'
    success_url = '/ex/'


from django.views.generic import DetailView

class Myview5(DetailView):
    model = Person
    # 템플릿을 지정하지않으면 모델이름_detail.html을 찾음.

from django.views.generic import ListView

class Myview6(ListView):
    model = Person
    # 템플릿: 모델이름_list.html



from django.views.generic import UpdateView

class Myview7(UpdateView):
    model = Person
    form_class = PersonModelForm
    # 템플릿: 모델이름_form.html
    success_url = '/ex/exam09/'

    def get_object(self):
        print('update처리')
        object = Person.object.get(pk=self.kwargs['pk'])
        self.success_url+= str(object.id)+'/'
        return object

from django.views.generic import DeleteView
from django.urls import reverse_lazy
class Myview8(DeleteView):
    model = Person
    # 템플릿: 모델이름_confirm_delete.html
    success_url = reverse_lazy('ex_form:exam09')
'''
generic뷰 오버라이딩 몇가지
get_context_data()
get_queryset()
get_form_class()
form_valid()
form)invalid()
get_success_url()
'''
