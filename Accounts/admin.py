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


admin.site.register (User, CustomeAdmin)