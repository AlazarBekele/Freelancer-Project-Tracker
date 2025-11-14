from django.contrib import admin
from .models import (
    Welcome,
    AccountTracker
)

from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register (Welcome)
admin.site.register (AccountTracker)


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'field_choose', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('field_choose',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('field_choose',)}),
    )

admin.site.register(User, CustomUserAdmin)