# User Profile and Picture

- Upload profile pic for users and learn how to use django signals to run specific functions after
certain actions
- By default there's no field for user picture. Extend the user model to add it.
- Create a new class `Profile`, which has a one to one relationship with the user model.That is,
each user can have only one profile and each profile is for one user only.
- To create a one-to-one relationship you can use the following:
  - `user = models.OneToOneRelationship(User, on_delete=models.CASCADE)`
  - here cascade means that if user is deleted, profile is also deleted but not the other way around.
- Since, models bring a change to the database, we have to make migrations.
- This is done in two steps: 
  - First a migration file create using `python manage.py make_migrations`
  - Then, the migration file is run using the command `python manage.py migrate`
- Now, if you wish to see the model/database in the admin page, you have to register it with the admin models.
  - Run this command to register with the admin: `admin.site.register(Profile)`
  
- For an image field:
  - BASE_DIR : A variable that django created for at the top of the settings file that specifies the location of projects's base directory.
  - **MEDIA_ROOT** is going to be the full path to a directory, where we'll tell django to store the uploaded files.
  - Add the below line at the ending of the settings.py file : `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
  - This tells django to have the media directory at the base location of the project.
  - MEDIA_URL is the public url of media directory. This is how we'll access media through the browser.
    - Add this at the end of settings file : `MEDIA_FILE = '/media/'`

- **Django signal**
  - To automatically create a profile whenever a user is created use django signals!
  - **post_save** is a signal that gets saved when an object is saved. Use this to command to import post_save:
    - `from django.db.models.signals import post_save`
  - Here user model is the sender, as it sends the signal upon saving and we want the receiver to do some action upon receving the signal.
  - After creating the functions, we have to import the signal inside of the ready function of users apps.py file in the UsersConfig class.
