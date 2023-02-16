from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .views_functions import *
from elegoua_engine import get_project

def homepage(request):
    return render(request, 'home.html')

def teampage(request):
    return render(request, 'team.html')

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

            # Get student project
            student_answer = {
                'level': {'auto_eval_level': int(python_level)},
                'interests': {
                    'main_interest': interest,
                    'other_interests': [],
                },
            }
            project = get_project.Project(student_answer)
            student_db, student_questions = project.define_project()
            
            # Debug print
            print(f'student_level: {student_db}')
            print(f'student_questions: {student_questions}')
            
            # Export data to csv
            form_data = [
                first_name,
                last_name,
                python_level,
                interest,
                student_db,
                student_questions
            ]
            export_form(form_data)

            return render(request, 'thanks.html')
    else:
        # Display empty form since the page has just been loaded
        form = ContactForm()

    return render(request, 'form.html', {'form': form})
