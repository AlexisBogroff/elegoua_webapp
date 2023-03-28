from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .views_functions import *
from elegoua_engine import get_project


def homepage(request):
    return render(request, 'home.html')

def originpage(request):
    return render(request, 'origins.html')

def demopage(request):
    return render(request, 'demo.html')

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
            group = form.cleaned_data['group']
            email= form.cleaned_data['email']
            interests= form.cleaned_data['interests']
            work_field=form.cleaned_data['work_field']
            python_level = form.cleaned_data['python_level']
            libraries_used=form.cleaned_data["libraries_used"]
            data_structures=form.cleaned_data["data_structures"]
            data_type_char=form.cleaned_data["data_type_char"]
            for_loop_syntax= form.cleaned_data["for_loop_syntax"]
            range_args=form.cleaned_data["range_args"]
            matrix_tool=form.cleaned_data['matrix_tool']
            hobbies=form.cleaned_data['hobbies']
            job=form.cleaned_data['job']
            level_of_detail=form.cleaned_data['level_of_detail']
            dico_test=form.cleaned_data['dico_test']
            condition=form.cleaned_data['condition']
            lenght=form.cleaned_data['lenght']
            arg_attributes=form.cleaned_data['arg_attributes']
            na_values_instruction=form.cleaned_data['na_values_instruction']
            ml_method=form.cleaned_data['ml_method']

            # Define dictionary to map choices to string values
            level_dico = {'1': 'Beginner', '2': 'Intermediate', '3': 'Advanced'}
            # Access selected choice and convert to string value
            python_level = level_dico[python_level]
            #Get student project
            interests = interests.split(';')
            hobbies = hobbies.split(';')
            student_answer = {
                'level': {'auto_eval_level': python_level},
                'interests': {
                    'main_interest': interests,
                    'other_interests': hobbies,
                },
            }
            print(student_answer)
            project = get_project.Project(student_answer)
            level,subject,dataset = project.define_project()  
            # Debug print
            print(f'student_level: {level}')
            print(f'student_subject: {subject}')
            
            # Export data to csv
            form_data = [first_name,last_name,python_level,subject,dataset]
            export_form(form_data)
            # student_db & student_question
            # dico = {'dataset_filename' : dataset_filename, 'question':question'}    
            dico = {"subject":subject,"level" : level,"dataset":dataset}
            return render(request, 'thanks.html',dico)
    else:
        # Display empty form since the page has just been loaded
        form = ContactForm()
        
    return render(request, 'form.html', {'form': form})