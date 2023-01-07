# Elegoua

## Current website design

Home page
<img width="1209" alt="Screenshot 2022-12-23 at 05 22 54" src="https://user-images.githubusercontent.com/31806900/209270609-f99fe206-1f40-4987-acec-09d7cfe840e2.png">

Form page
<img width="1210" alt="Screenshot 2022-12-23 at 05 23 10" src="https://user-images.githubusercontent.com/31806900/209270631-34d36d26-9a9f-48a0-86d1-772955f92836.png">

## Current webiste capabilities
- Display home page
- Get information via a userform
- Display a contact page

## Current backend capabilities
- Store user data into a csv file

------------

## Project Setup

### Create separate development environment
```
conda create -n django_test python=3.9
conda activate django_test
```

### Install django
```
conda install django
```

### Install package elegoua_engine
cf. https://github.com/AlexisBogroff/CheatSheets/blob/master/PythonPackaging.md
Select a location to store the package elegoua_engine
```
git clone https://github.com/AlexisBogroff/elegoua_engine.git
cd elegoua_engine
python setup.py develop
```

### Clone and launch webapp
Select an other location to store elegoua_webapp
```
git clone https://github.com/AlexisBogroff/elegoua_webapp.git
cd elegoua_webapp
cd elegoua
git checkout dev
python manage.py runserver
```

### Go to website
http://127.0.0.1:8000/webapp/home/
