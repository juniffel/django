from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
def index(request):
    # return HttpResponse('Index')
    now = timezone.now()
    context = {
        'now':now,
        'name':'홍기르동무',
    }
    return render(request,'index.html',context)

