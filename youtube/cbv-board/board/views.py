from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Board
from.forms import BoardSearchForm

from django.db.models import Q

class BoardSearch(generic.ListView):
    model = Board
    # paginate_by = 3
    object_list_size = 0

    def  get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword:
            object_list = Board.objects.filter(
                Q(title__icontains=keyword)|
                Q(content__icontains=keyword)
            ).order_by('-pk')
            self.object_list_size = object_list.count()
            return object_list
        else:
            return Board.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = BoardSearchForm()
        context['keyword'] = self.request.GET.get('keyword')
        context['object_list_size'] = self.object_list_size
        return context
class BoardList(generic.ListView):
    model = Board
    ordering = ['-pk']
    # paginate_by =2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searxh_form'] = BoardSearchForm()
        return context

from.forms import BoardForm
from django.urls import reverse_lazy,reverse

class BoardCreate(generic.CreateView):
    model = Board
    form_class =BoardForm
    success_url = reverse_lazy('board:list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_label'] = '등록'

        return context

class BoardDetail(generic.DetailView):
    model = Board

    def get_object(self, queryset = None):
        item = super().get_object(queryset)
        item.incrementReadCount()
        return item


from.forms import BoardUpdateForm

class BoardUpdate(generic.UpdateView):
    model = Board
    form_class = BoardUpdateForm
    success_url = reverse_lazy('board')

    def get_success_url(self) :
        return reverse('board:detail', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_label'] = '수정'

        return context

class BoardDelete(generic.DeleteView):
    model = Board
    success_url = reverse_lazy('board:list')
