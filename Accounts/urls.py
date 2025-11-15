from django.urls import path
from .views import (
    index,
    loginPage,
    goto_pass
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('welcome/', index, name='Index'),
    path ('login/', loginPage, name='Login'),
    path ('gotopass/', goto_pass, name='Pass')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)