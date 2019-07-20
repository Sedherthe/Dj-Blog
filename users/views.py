from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# After submission
			print("details are : ", request.POST)
			form.save() # If everythign is okay
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('blog-home')
	else: 
		form = UserCreationForm()
	return render(request, 'users/registration.html', {'form': form})