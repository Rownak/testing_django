from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required

	# Create a form
	# What messages to shwo
	# messages.debug
	# messages.info
	# messages.success
	# messages.warning
	# messages.error
	#
	#this form is provided by django to use

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been created for {username}! You are now able to login!')
			return redirect('login')
	else:
		form = UserRegisterForm()

	# You need to create a template "users/register.html" that uses the form
	return render(request, 'users/register.html', {'form': form})

# @login_required is a decorator
# Basically its adds functionality to our profile viwe
@login_required
def profile(request):
	return render(request, 'users/profile.html')

