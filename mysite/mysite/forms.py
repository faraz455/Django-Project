from attr import attr
from django import forms

class UserForms(forms.Form):
    num1 =  forms.CharField(label="Value 1", widget=forms.TextInput(attrs={'class': 'form-control'}))
    num2 = forms.CharField(label="Value 2", widget=forms.TextInput(attrs={'class': 'form-control'}))