from django.contrib import admin
from .models import (
    Welcome,
    AccountTracker,
    GoInto,
    ProfilePicture,
    Profiles,
    User
)

from django.contrib.auth.admin import UserAdmin

# Import the Orignal User
from django.contrib.auth.models import User as OriginalUser
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin

# Register the Orginal User
admin.site.register (OriginalUser, OriginalUserAdmin)

class ProfileAddUser (admin.StackedInline):

    model = Profiles

class CustomeAdmin (UserAdmin):

    inlines = [ProfileAddUser]
    model = User

# Register your models here.

admin.site.register (Welcome)
admin.site.register (AccountTracker)
admin.site.register (GoInto)
admin.site.register (ProfilePicture)
admin.site.register (Profiles)

# User Add Field

admin.site.register (User, CustomeAdmin)