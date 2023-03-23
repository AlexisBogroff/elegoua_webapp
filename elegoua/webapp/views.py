from django.shortcuts import render
from django.http import HttpResponse
from elegoua_engine import get_project
from .forms import ContactForm
from .views_functions import *


def homepage(request):
    return render(request, 'home.html')

def contactpage(request):
    return render(request, 'contact.html')

def thankspage(request):
    return render(request, 'thanks.html')
def ProjectOriginspage(request):
    return render(request,'ProjectOrigins.html' )
def Demopage(request):
    return render(request,'Demo.html')

def formpage(request):
    if request.method == 'POST':
        # Extract and process filled up data        
        form = ContactForm(request.POST)
        if form.is_valid():
            project=get_project.Project(form.cleaned_data)
            # Get data from each form field         
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
            groupe_TD = form.cleaned_data['groupe_TD']
            email= form.cleaned_data['email']
            quelles_sont_vos_passions= form.cleaned_data['quelles_sont_vos_passions']
            dans_quel_domaine_voulez_vous_travailler=form.cleaned_data['dans_quel_domaine_voulez_vous_travailler']
            python_level = form.cleaned_data['python_level']
            quelles_librairies_avez_vous_deja_utilisees=form.cleaned_data["quelles_librairies_avez_vous_deja_utilisees"]
            quelles_structures_de_donnees_connaissez_vous=form.cleaned_data["quelles_structures_de_donnees_connaissez_vous"]
            quel_est_le_type_de_données_pour_un_caractere_en_python=form.cleaned_data["quel_est_le_type_de_données_pour_un_caractere_en_python"]
            quelle_est_la_syntaxe_d_une_boucle_for_pour_parcourir_les_elements_d_une_liste_L= form.cleaned_data["quelle_est_la_syntaxe_d_une_boucle_for_pour_parcourir_les_elements_d_une_liste_L"]
            quels_sont_les_arguments_de_la_fonction_range=form.cleaned_data["quels_sont_les_arguments_de_la_fonction_range"]
            quel_est_l_outil_le_plus_rapide_pour_faire_des_calculs_sur_une_matrice=form.cleaned_data['quel_est_l_outil_le_plus_rapide_pour_faire_des_calculs_sur_une_matrice']
            quelles_sont_vos_activites_extrascolaires=form.cleaned_data['quelles_sont_vos_activites_extrascolaires']
            quul_metier_envisagez_vous=form.cleaned_data['quel_metier_envisagez_vous']
            préferez_vous_des_instructions_détailles_ou_des_indications_larges_pour_votre_projet=form.cleaned_data['préferez_vous_des_instructions_détailles_ou_des_indications_larges_pour_votre_projet']
            qu_est_ce_qu_on_utilise_pour_avoir_acces_a_une_valeur_dans_un_dictionnaire=form.cleaned_data['qu_est_ce_qu_on_utilise_pour_avoir_acces_a_une_valeur_dans_un_dictionnaire']
            quels_mots_cles_permettent_de_verifier_une_condition=form.cleaned_data['quels_mots_cles_permettent_de_verifier_une_condition']
            quelle_fonction_permet_de_determiner_la_taille_d_un_dataframe=form.cleaned_data['quelle_fonction_permet_de_determiner_la_taille_d_un_dataframe']
            quel_argument_permet_d_acceder_aux_attributs_d_un_objet_dans_une_methode_de_classe=form.cleaned_data['quel_argument_permet_d_acceder_aux_attributs_d_un_objet_dans_une_methode_de_classe']
            quelle_instruction_permet_d_avoir_le_nombre_total_de_valeurs_NA_pour_chaque_variable_d_un_dataframe_df=form.cleaned_data['quelle_instruction_permet_d_avoir_le_nombre_total_de_valeurs_NA_pour_chaque_variable_d_un_dataframe_df']
            quelle_methode_permet_d_identifier_les_meilleurs_parametres_d_un_modele_ML=form.cleaned_data['quelle_methode_permet_d_identifier_les_meilleurs_parametres_d_un_modèle_ML']

            # Get student project
            student_answer = {
                'level': {'auto_eval_level': int(python_level)},
                'interests': {
                    'main_interest':[],
                    'other_interests': [],
                },
            }
            project = get_project.Project(student_answer)
            student_db, student_questions = project.define_project()            
            # Debug print
            print(f'student_level: {student_db}')
            print(f'student_questions: {student_questions}')
            # Export data to csv
            form_data =   []                                                                              
            
            export_form(form_data)
            return render(request, 'thanks.html')
    else:
        # Display empty form since the page has just been loaded
        form = ContactForm()

    return render(request, 'form.html', {'form': form})
