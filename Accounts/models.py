from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User as orginalUserModel

from django.utils import timezone
from datetime import timedelta

# Create your models here.
# Extract the User Profile's

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


class Profiles (models.Model):

    user = models.OneToOneField (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_profile_img = models.ImageField (upload_to='profile_pic/', null=True, blank=True)

    # Follow People
    follow_suggetion = models.ManyToManyField ("self", related_name="followed_by", symmetrical=False, blank=True, null=True)
    last_seen = models.DateTimeField (auto_now=True, blank=True, null=True)

    def is_online (self):

        if self.last_seen:
            
            return timezone.now() - self.last_seen < timedelta(minutes=5)
        
        return False

    def __str__(self):
        return self.user.username
    
    note_forms = models.CharField (max_length=100, null=True, blank=True)
    

class Follow (models.Model):

    followers = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")
    

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
    

class Make_Publish_Post (models.Model):

    Title = models.CharField (max_length=100, null=False, blank=False)
    Discription = models.TextField (null=True, blank=True)
    Publish_IMG = models.ImageField (upload_to='UserPost/Published')

    # Count Like & collect Messages
    Rate = models.IntegerField ()
    Messages = models.CharField (max_length=255)