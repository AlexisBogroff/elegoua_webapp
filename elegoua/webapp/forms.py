from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    python_level = forms.CharField(max_length=300)
    interest = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':45}))

