from django.shortcuts import render
from .forms import UploadFileForm
# Create your views here.
def index(request):
    return render(request, 'ex_upload/index.html')

from django.shortcuts import reverse, redirect

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data
            form.save()
            return redirect(reverse('ex_upload:index'))
    else:
        form = UploadFileForm()

    return render(request, 'ex_upload/upload_form.html', {'form':form})

from .models import UploadFile
def file_list(request):
    list = UploadFile.objects.all().order_by('-pk')
    return render(
        request,
        'ex_upload/file_list.html',
        {'list':list}
    )

import os
from django.conf import settings
def delete_file(request,id):
    file = UploadFile.objects.get(pk=id)
    media_root = settings.MEDIA_ROOT
    remove_file = media_root+'/'+str(file.file)
    print('삭제할 파일:', remove_file)
    if os.path.isfile(remove_file):
        os.remove(remove_file) #실제 파일삭제
    file.delete()# db삭제

    return redirect(reverse('ex_upload:list'))
