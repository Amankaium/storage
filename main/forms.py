from django import forms
from .models import *

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        exclude = ('id',)


class GoodSoldForm(forms.Form):
    qty = forms.IntegerField(label='Количество')
