from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre # 사용할 모델 클래스

def index(request):
    """사이트의 홈 페이지에 대한 보기 기능입니다."""

    # 일부 주요 객체의 개수 생성
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # 이용 가능한 도서 (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # 기본적으로 'all()'이 암시됩니다.
    num_authors = Author.objects.count()

    num_sf = Book.objects.filter(genre__name__icontains='SF').count() # 과제로 내가 추가 해본것

    # 세션 변수에 계산된 이 보기에 대한 방문 횟수입니다.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'num_sf' : num_sf,
    }

    # 컨텍스트 변수의 데이터로 HTML 템플릿 index.html을 렌더링합니다.
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    # 템플릿에서 사용할 변수명을 지정할 수 있음.(지정하지 않으면 modelname_list 또는 object_list)
    # context_object_name = 'my_book_list'
    # 템플릿 에서 사용할 데이터를 지정할 수 있음(지정하지 않으면 전부 사용가능)
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # 템플릿 이름을 명시 할 수 있음.(명시하지 않으면 자동 서칭)
    # template_name = 'books/my_arbitrary_template_name_list.html'
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    # paginate_by = 3

class AuthorDetailView(generic.DetailView):
    model = Author

# 대출한 책 보기
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )
from django.contrib.auth.mixins import PermissionRequiredMixin


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """사서가 특정 BookInstance를 갱신하는 기능을 봅니다."""
    # 키값에 해당하는 레코드를 반환하거나 에러를 반환
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # POST 요청인 경우 양식 데이터를 처리합니다.
    if request.method == 'POST':

        # 양식 인스턴스를 생성하고 요청(바인딩)의 데이터로 채웁니다.
        form = RenewBookForm(request.POST)

        # 양식이 유효한지 확인합니다.
        if form.is_valid():
            # 필요에 따라 form.cleaned_data의 데이터를 처리합니다. (여기서는 모델의 Due_back 필드에 기록합니다.)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # 새 URL로 리디렉션:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # GET(또는 다른 방법)인 경우 기본 양식을 만듭니다.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'05/01/9999',}
    permission_required = 'catalog.add_author'

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    permission_required = 'catalog.change_author'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.delete_author'

# 책 등록, 수정,삭제
class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.add_book'

class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    # 권장하지 않음(더 많은 필드를 추가하면 보안 문제가 발생할 수 있음)
    fields = '__all__'
    permission_required = 'catalog.change_book'

class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.delete_book'
