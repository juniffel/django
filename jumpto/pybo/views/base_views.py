from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q


def index(request):
    # 페이지 가져오기
    page = request.GET.get("page", "1")
    kw = request.GET.get("kw", "")  # 검색어
    # 생성일 역순으로 질문 목록이 담긴 리스트
    question_list = Question.objects.order_by("create_date")
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)  # 제목 검색
            | Q(content__icontains=kw)  # 내용 검색
            | Q(answer__content__icontains=kw)  # 답변 내용 검색
            | Q(author__username__icontains=kw)  # 질문 글쓴이 검색
            | Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    # 페이지네이터 : 질문 리스트 10개씩 표시
    paginator = Paginator(question_list, 10)
    # 페이지 객체 : 질문 10개를 표시한 1페이지
    page_obj = paginator.get_page(page)
    template_name = "pybo/question_list.html"
    context = {"question_list": page_obj, "page": page, "kw": kw}
    return render(request, template_name, context)


def detail(request, question_id):
    # 없는 데이터에 대한 요청처리를 위해 get_object_or_404 사용
    # question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk=question_id)
    template_name = "pybo/question_detail.html"
    context = {"question": question}
    return render(request, template_name, context)
