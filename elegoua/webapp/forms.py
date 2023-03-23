from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    group = forms.CharField(max_length=100)
    email = forms.EmailField (max_length =200)
    python_level_choices = (('1','Beginner'),('2','intermediate'),('3','advanced'))
    python_level = ChoiceField(widget=RadioSelect, choices=python_level_choices)
    interest = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':45}))

    