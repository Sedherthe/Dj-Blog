from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

"""
	Options with messages:
		message.debug
		message.info
		message.warning
		message.success
		message.error
"""

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			# After submission
			print("details are : ", request.POST)
			form.save() # If everythign is okay
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created successfully. You can now Log In!')
			return redirect('user-login')
	else: 
		form = UserRegisterForm()
	return render(request, 'users/registration.html', {'form': form})
