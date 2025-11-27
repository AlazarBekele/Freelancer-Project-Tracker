from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# Extract the User Profile's

class User(AbstractUser):

    field_choose = models.CharField (max_length=30, null=True, blank=True)

class Profile (models.Model):

    # By what extraction method do you use my extraction (Choose field 'client', 'freelancer')

    ROLE_CHOICE = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer')
    )

    user = models.OneToOneField (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField (max_length=20, choices=ROLE_CHOICE)

    def __str__(self):
        return self.user.username
    

class ProfilePicture (models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userProfile = models.ImageField(upload_to='Profile_picture/')

    def __str__(self):
        return self.user.username


class Welcome (models.Model):

    Title = models.CharField (max_length=30)
    IMG = models.ImageField (upload_to='Welcome/')

    def __str__(self):
        return self.Title


class AccountTracker (models.Model):

    Field = models.CharField (max_length=20)

    def __str__(self):
        return self.Field
    

class GoInto (models.Model):

    DashName = models.CharField (max_length=20)
    DashIMG = models.ImageField (upload_to='GoInto/')

    def __str__(self):
        return self.DashName
    

class Work_fields (models.Model):

    work_flow = models.CharField (max_length=60, null=True, blank=True)