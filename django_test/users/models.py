from django.db import models
# extending default user model
from django.contrib.auth.models import User

class Profile(models.Model):
	# if user get deleted also delet the profile
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# add other field

	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	# What to display if user is printed
	def __str__(self):
		return f'{self.user.username} Profile'

