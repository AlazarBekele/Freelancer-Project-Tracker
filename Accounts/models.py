from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# Extract the User Profile's

class Profiles (models.Model):

    # By what extraction method do you use my extraction (Choose field 'client', 'freelancer')

    ROOL_CHOOSE = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer')
    )

    user = models.OneToOneField (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField (max_length=20, choices=ROOL_CHOOSE)

    def __str__(self):
        return self.user.username

class User(AbstractUser):

    field_choose = models.CharField (max_length=30, null=True, blank=True)
class Welcome (models.Model):

    Title = models.CharField (max_length=30)
    IMG = models.ImageField (upload_to='Welcome/')

    def __str__(self):
        return self.Title


class ProfilePicture (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userProfile = models.ImageField (upload_to='Profile_picture/')

    def __str__(self):
        return self.user.username


class AccountTracker (models.Model):

    Field = models.CharField (max_length=20)

    def __str__(self):
        return self.Field
    

class GoInto (models.Model):

    DashName = models.CharField (max_length=20)
    DashIMG = models.ImageField (upload_to='GoInto/')

    def __str__(self):
        return self.DashName