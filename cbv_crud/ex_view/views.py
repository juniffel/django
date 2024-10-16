from django.shortcuts import render,reverse
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from . models import Info
from .forms import PersonModelForm
from django.urls import reverse_lazy

class Index(ListView):
  model = Info

  def get_template_names(self) -> list[str]:
    print(f" 템플릿 이름:{super().get_template_names()}")
    return super().get_template_names()


class Detail(DetailView):
  model = Info

class Update(UpdateView):
  model = Info
  form_class = PersonModelForm

  def get_success_url(self):
    # 수정된 객체의 pk를 사용하여 상세보기 페이지 URL 생성
    return reverse('ex_view:detail', kwargs={'pk': self.object.pk})


class Delete(DeleteView):
  model = Info
  success_url = '/ex/index/'

class Create(CreateView):
  model = Info
  form_class = PersonModelForm
  template_name = 'ex_view/info_create.html'
  success_url = '/ex/index/'
