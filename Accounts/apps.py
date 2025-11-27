from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Accounts'

<<<<<<< HEAD
    def ready(self):
        import Accounts.signals
=======
def ready(self):

    import Accounts.signals
>>>>>>> New-Code
