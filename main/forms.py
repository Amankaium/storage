from django import forms
from .models import *

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        exclude = ('id',)


class GoodSoldForm(forms.Form):
    qty = forms.IntegerField(label='Количество')


class GoodAddForm(forms.Form):
    name = forms.CharField(
        max_length=255, label='Наименование товара',
        help_text='Cтатус по умолчанию - "Нет в наличии" и количество равно 0')
