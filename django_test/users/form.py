from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# this class inherits from UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	# This class gives us a nested namespace for configuration
	# keeps the configeration in one place 
	class Meta:
		# user model means when we do form.save() it is going to save data
		# in user model
		# And the field we have here are the fields that we want in the
		# form and in what order 
		model = User
		fields = ['username', 'email', 'password1', 'password2']