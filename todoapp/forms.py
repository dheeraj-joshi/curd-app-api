from django import forms
from .models import CreateModel



class CreationForm(forms.ModelForm):
     class Meta:
        model=CreateModel
        fields=['tittle','content','completed','acheive']

class UpdateForm (CreationForm):  
    class Meta:
        model=CreateModel
        fields='__all__' 
        exclude = ('created_at',)    