from django.shortcuts import render

# Create your views here.
from .models import Info

def list(request):
    info_lsit = Info.objects.all()
    context = {
        'info_list':info_lsit,
    }

    return render(request, 'ex_model/list.html', context)
