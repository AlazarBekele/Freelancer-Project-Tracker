from django.urls import path
from .views import (
    index,
    loginPage,
    goto_pass,
    freelancer_page,
    crud_info,
    publish_page_both
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', index, name='Index'),
    path ('login/', loginPage, name='Login'),
    path ('gotopass/', goto_pass, name='Pass'),
    path ('FTP.com.admin/<int:id>', freelancer_page, name='Freelancers'),
    path ('Update/<str:username>', crud_info, name='update'),
    path ('publish/<str:username>', publish_page_both, name='post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)