from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.conf import settings

# Create your models here.

# By what extraction method do you use my extraction (Choose field 'client', 'freelancer')
ROLE_CHOICE = (
    ('client', 'Client'),
    ('freelancer', 'Freelancer')
)

WORK_ON = [
    ('website', 'Website'),
    ('videoEditer', 'Video Editor'),
    ('AccountFinace', 'Account Finace'),
    ('websitedesign', 'Website Design'),
    ('HR', 'Human Resource'),
    ('software', 'Software Engineering'),
]

class User(AbstractUser):

    field_choose = models.CharField (max_length=30, null=True, blank=True)
    working_fields = models.CharField (max_length=30, null=True, blank=True)


class AccountInfo (AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField (max_length=20, null=True,blank=True)
    last_name = models.CharField (max_length=20, null=True,blank=True)

    # Username & Email Fields
    username = models.CharField (max_length=8, unique=True, null=True,  blank=True)
    email = models.EmailField (unique=True)

    # Work Flow & Role Choices
    field_choose = models.CharField (max_length=20, choices=ROLE_CHOICE)
    working_fields = models.CharField (max_length=20, choices=WORK_ON)

    # Password & Confirm
    password1 = models.CharField (max_length=10)
    password1 = models.CharField (max_length=10)

class Profiles (models.Model):

    user = models.OneToOneField (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_profile_img = models.ImageField (upload_to='profile_pic/', null=True, blank=True)

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