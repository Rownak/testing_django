from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
    	#django documentation recommend to add this for signal
    	import users.signals
