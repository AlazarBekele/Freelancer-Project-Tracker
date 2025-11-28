from django.contrib import admin
from .models import (
    Welcome,
    AccountTracker,
    GoInto,
    ProfilePicture,
    Profiles
)

from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register (Welcome)
admin.site.register (AccountTracker)
admin.site.register (GoInto)
admin.site.register (ProfilePicture)
admin.site.register (Profiles)

admin.site.unregister (Group)

class ProfileAddUser (admin.StackedInline):

    model = Profiles

class CustomeAdmin (UserAdmin):

    inlines = [ProfileAddUser]
    model = User
    fields = ['role', 'work_field_flows']

# register the Make
admin.site.register (User, CustomeAdmin)