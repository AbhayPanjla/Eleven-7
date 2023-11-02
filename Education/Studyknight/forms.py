from django import forms
from Studyknight.models import SSC

class InputForm(forms.Form):
    for_txt = forms.CharField(max_length=200)

class InputForm(forms.Form):
    for_run = forms.CharField(max_length=400)    
class Nameform(forms.Form):
    show_name = forms.CharField(label="show_name", max_length=100)
class Meta:
    model = SSC
    feilds = "__all__"
   
