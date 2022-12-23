import csv
import os

def export_form(form_data:list):
    """ Export data into a csv file """
    
    with open('webapp/data/form/form_data.csv', 'a') as f:
        write = csv.writer(f, delimiter =";")
        write.writerows([form_data])
