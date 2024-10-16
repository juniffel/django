from django.shortcuts import render,reverse
from django.urls import  reverse_lazy
from django.views import generic
from .models import Board
from .forms import BoardForm, BoardUpdateForm

class BoardList(generic.ListView):
  model = Board
  ordering = ['-pk'] # 정렬 순서 (최신글이 위에 오게)4

class BoardCreate(generic.CreateView):
  model = Board
  form_class = BoardForm
  success_url = reverse_lazy('board:list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["button_label"] = '등록'
    return context

class BoardDetail(generic.DetailView):
  model = Board

  # 조회수 증가
  def get_object(self,):
    item = super().get_object()
    item.increment_read_count()
    return item

class BoardUpdate(generic.UpdateView):
  model = Board
  form_class = BoardUpdateForm
  # success_url = reverse_lazy("board:list")
  def get_success_url(self):
    return reverse('board:detail' , args=(self.object.id))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["button_label"] = '수정'
    return context

class BoardDelete(generic.DeleteView):
  model = Board
  success_url =  reverse_lazy('board:list')
