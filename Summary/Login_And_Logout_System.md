# Login and Logout System

- Django has a lot of functionality taking care of this system in the bakcend already.
- To import login and logout views use the below command 
  - `from django.contrib.auth import views as auth_views`
- Login views : auth_views.LoginView.as_view()
- Logout views: auth_views.LogoutView.as_view()
- These are **class based** views. These are gonna handle all the forms and logic for us but not the templates.
- By default it looks at `registration/login.html` for the template.
- You can pass any new path for django, in the as_view function. For example, 
  - `template_name='users/login.html'`
- By defualt, django redirects to profile page after a successful login. To change this add the following line to the settings.y file:
  - `LOGIN_REDIRECT_URL = 'blog-home'` (*Here blog-home is the name for a url*)
- We can check if a user is logged in using:
  - `is_authenticated`
  
  ## Profile
  
- Django has a inbuilt variable **user**, that holds the details about the logged in user.
- Django also provides a login decorator, which will check or proceed only if a user is logged in.
  - So, if a user is not logged in, the user will be redirected to the login page.
- Default login url is `accounts/login`, so it redirects to this url for login by default.
- Change it the required url by adding the below line at the end of settings.py file:
  - `LOGIN_URL = 'user-login'`
