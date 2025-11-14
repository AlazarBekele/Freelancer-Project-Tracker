from django.contrib import admin
from .models import (
    Welcome,
    AccountTracker
)
# Register your models here.

admin.site.register (Welcome)
admin.site.register (AccountTracker)