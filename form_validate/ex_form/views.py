from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Person
from .forms import PersonForm

def exam01(request):
  if request.method=='POST':
    name = request.POST['name']
    age = request.POST['age']
    print(name,age)
    Person(name=name,age=age).save()
    print(Person.objects.all())
    return redirect(reverse('ex_form:exam01'))
  else:
    return render(request,
        'ex_form/exam01.html',
        )


def exam02(request):
  if request.method=='POST':
    personForm = PersonForm(request.POST)
    if personForm.is_valid(): # 유효성 검사
      name = personForm.cleand_data['name']
      age = personForm.cleand_data['age']
      print(f"이름:{name},나이:{age}")
      Person(name=name,age=age).save()
      print(f"모델 데이터 확인:{Person.objects.all()}")
      return redirect(reverse('ex_form:exam02'))
    else:
      return render(request,
        'ex_form/exam02.html',
        {'form':personForm}
        )
  else:
    form = PersonForm()
    return render(request,
        'ex_form/exam02.html',
        {'form':form}
        )

from . forms import PersonModelForm

# 모델 폼 클래스 적용
def exam03(request):
  if request.method =='POST':
    form= PersonModelForm(request.POST)
    if form.is_valid():
      form.save() # 모델 폼을 사용하면 클린데이터를 꺼내고 자시고 할 필요가 없음.
      return HttpResponse('처리완료')
  else:
    form=PersonModelForm()
  return render(request,
                'ex_form/exam03.html',
                {'form':form})
