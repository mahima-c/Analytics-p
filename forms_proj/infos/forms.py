from django import forms
from .models import *

class InfoModelForm(forms.ModelForm):
    class Meta:
        model=Info
        fields=('name','description',)

