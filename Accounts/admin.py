from django.contrib import admin
from .models import (
    Welcome,
    AccountTracker,
    GoInto,
    ProfilePicture,
    Profiles
)

from django.contrib.auth.models import Group

from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register (Welcome)
admin.site.register (AccountTracker)
admin.site.register (GoInto)
admin.site.register (ProfilePicture)
admin.site.register (Profiles)

class ProfileAddUser (admin.StackedInline):

    model = Profiles

class UserAdmin (admin.ModelAdmin):

    model = User
    fields = ['first_name', 'last_name', 'email', 'user_name', 'role', 'work_field_flows']
    inlines = [ProfileAddUser]

# unregister the default one
admin.site.unregister (User)

# register the Make
admin.site.register (User, UserAdmin)


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'field_choose', 'working_fields', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('field_choose',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('working_fields',)}),
    )

admin.site.register(User, CustomUserAdmin)