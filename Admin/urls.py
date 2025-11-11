from django.urls import path
from .views import (
    index,
    loginPage
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', index, name='Index'),
    path ('login/', loginPage, name='Login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)