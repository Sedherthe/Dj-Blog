# User Registration

  - Create a new Users app to handle.
  - When we first create a new app, let's add this immediately to the installed apps list in the project settings file.

## Registration

  - For registration Django provides **User Creation** class that will get converted to html form.
  - Create a template to handle the user registration which would extend the base template and extend it with the form.
  - Don't forget to add a csrf token, which adds security and is compulsory. 
  
## Creating A Custom Form Class
  
  - Import the stanadard class from django
  - Add all the fields you want.
  - Define the class **Meta** which gives a nested namespace, for configuration and keeps the configurations in one place     
    - Define the model in the class that will be affected.
    - And the fields that we want in the form and in what order.  
    
## Add Crispy forms app for more neat looking forms
- Install using pip install django-crispy-forms
- Add the installed app **crispy_forms** to the installed apps list in settings.py
- Also by default the crispy forms uses bootstrap 2. So change the template by adding the below given line at the ending of the settings.py file
  - `CRISPY_TEMPLATE_PACK = 'bootstrap4'`
