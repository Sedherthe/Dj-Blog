from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
	# Because we haven't given any action field to the form on the registration page, it'll be
	# redirected to the same page as it is currently present.
	if request.method == 'POST':
		print("requested POST method: ", request)
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
	print("form is: ", form)
	return render(request, 'users/registration.html', {'form': form})

# Using a decorator which makes login mandatory for this view.(profile)
@login_required
def profile(request):

	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			print(request.user.profile.image.path)
			p_form.save()
			print(request.user.profile.image.path)
			print(f'Profile Successfully Updated!')
			messages.success(request, f'Profile Updated Successfully!')
			# Post Get redirect pattern problem. are you sure you wanna reload problem.
			return redirect('user-profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form' : u_form, 
		'p_form' : p_form
	}

	return render(request, 'users/profile.html', context)