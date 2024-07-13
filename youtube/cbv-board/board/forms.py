from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'writer', 'content']

class BoardUpdateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'writer', 'content']

    writer = forms.CharField(disabled = True)

class BoardSearchForm(forms.Form):
    keyword = forms.CharField(label='키워드', required = True)
    
