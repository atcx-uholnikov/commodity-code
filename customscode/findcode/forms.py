from django import forms
from .models import *

#Create a Goods form

class GoodsForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)



