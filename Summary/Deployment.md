# Deploying the Django app on Heroku

## What is Heroku and how does it work?

- Heroku runs Django websites within one or more "Dynos", which are isolated, virtualized Unix containers that provide the environment required to run an application. 
The dynos are completely isolated and have an ephemeral file system (a short-lived file system that is cleaned/emptied every time the dyno restarts).The only thing that dynos share by default are application configuration variables.
- In order to execute your application Heroku needs to be able to set up the appropriate environment and dependencies, and also understand how it is launched. 
For Django apps we provide this information in a number of text files:

  - **runtime.txt**: the programming language and version to use.
  - **requirements.txt**: the Python component dependencies, including Django.
  - **Procfile**: A list of processes to be executed to start the web application. For Django this will usually be the Gunicorn web application server (with a .wsgi script).
  - **wsgi.py**: WSGI configuration to call our Django application in the Heroku environment.
- Developers interact with Heroku using a special client app/terminal, which is much like a Unix bash script.This allows you to upload code that is stored in a git repository, inspect the running processes, see logs, set configuration variables and much more!
(*Expecting that this is setup already :) *)

## Creating an application repository in Github

- In order to get our application to work on Heroku we'll need to put our Django web application into a git repository, add the files above, integrate with a database add-on, and make changes to properly handle static files.
- Since you are already on github, now, I'm assuming that the app is already set up as a github repo.:)

## Updating the app for Heroku - The Process

- While Heroku's Getting Started on Heroku with Django instructions assume you will use the Heroku client to also run your local development environment, 
the changes mentioned here will be compatible with the existing Django development server.

### **Procfile**

- Create the file Procfile (no extension) in the root of your GitHub repository to declare the application's process types and entry points.Copy the following text into it:
  - `web: gunicorn locallibrary.wsgi --log-file -`
### **Gunicorn**

- Gunicorn is the recommended HTTP server for use with Django on Heroku (as referenced in the Procfile above). It is a pure-Python HTTP server for WSGI applications that can run multiple Python concurrent processes within a single dyno (see Deploying Python applications with Gunicorn for more information).
- Install Gunicorn locally on the command line using pip:
  - `pip3 install gunicorn`
  
### Database Configuration

- We can't use the default SQLite database on Heroku because it is file-based, and it would be deleted from the ephemeral file system every time the application restarts (typically once a day, and every time the application or its configuration variables are changed).
- To counter this, the database connection information is supplied to the web dyno using a configuration variable named DATABASE_URL. Rather than hard-coding this information into Django, Heroku recommends that developers use the dj-database-url package to parse the DATABASE_URL environment variable and automatically convert it to Django’s desired configuration format. 
- In addition to installing the dj-database-url package we'll also need to install psycopg2, as Django needs this to interact with Postgres databases.
- Install dj-database-url locally so that it becomes part of our requirements for Heroku to set up on the remote server, using pip:
  - `pip3 install dj-database-url`
- Also add the following lines to the bottom of the settings.py file in the main project directory:
  - `import dj_database_url`
  - `db_from_env = dj_database_url.config(conn_max_age=500)`
  - `DATABASES['default'].update(db_from_env)`

### Serving Static Files in production

- Serving static files via Django/web application is inefficient because the requests have to pass through unnecessary additional code (Django) rather than being handled directly by the web server or a completely separate CDN. While this doesn't matter for local use during development, it would have a significant performance impact if we were to use the same approach in production. 
- To make it easy to host static files separately from the Django web application, Django provides the collectstatic tool to collect these files for deployment (there is a settings variable that defines where the files should be collected when collectstatic is run).
- The relevant setting variables are:

    - **STATIC_URL**: This is the base URL location from which static files will be served, for example on a CDN. This is used for the static template variable that is accessed in our base template (see Django Tutorial Part 5: Creating our home page).
    - **STATIC_ROOT**: This is the absolute path to a directory where Django's "collectstatic" tool will gather any static files referenced in our templates. Once collected, these can then be uploaded as a group to wherever the files are to be hosted.
    - **STATICFILES_DIRS**: This lists additional directories that Django's collectstatic tool should search for static files.
  - In the settings.py file add the following lines:
    - `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`
    - `STATIC_URL = '/static/'`

### Whitenoise

- There are many ways to serve static files in production (we saw the relevant Django settings in the previous sections). Heroku recommends using the WhiteNoise project for serving of static assets directly from Gunicorn in production.
- Install whitenoise locally using the following command:
  - `pip3 install whitenoise`
- To install WhiteNoise into your Django application, open /locallibrary/settings.py, find the MIDDLEWARE setting and add the WhiteNoiseMiddleware near the top of the list, just below the SecurityMiddleware:
  - `'whitenoise.middleware.WhiteNoiseMiddleware',`

### Requirements

- The Python requirements of your web application must be stored in a file requirements.txt in the root of your repository. Heroku will then install these automatically when it rebuilds your environment. You can create this file using pip on the command line (run the following in the repo root):
  - `pip3 freeze > requirements.txt`
  
### Runtime

- The runtime.txt file, if defined, tells Heroku which programming language to use. Create the file in the root of the repo and add the following text:
  - `python-{version}`
  
## Now save the changes to the github repo and we're almost ready!



