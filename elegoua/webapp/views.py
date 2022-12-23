from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .views_functions import *

def homepage(request):
    return render(request, 'home.html')

def contactpage(request):
    return render(request, 'contact.html')

def thankspage(request):
    return render(request, 'thanks.html')


def formpage(request):
    if request.method == 'POST':
        # Extract and process filled up data
        
        form = ContactForm(request.POST)
        if form.is_valid():
            
            # Get data from each form field
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            python_level = form.cleaned_data['python_level']
            interest = form.cleaned_data['interest']

            # Make it a list
            form_data = [first_name, last_name, python_level, interest]
            
            # Export data to csv
            export_form(form_data)

            return render(request, 'thanks.html')
    else:
        # Display empty form since the page has just been loaded
        form = ContactForm()

    return render(request, 'form.html', {'form': form})
