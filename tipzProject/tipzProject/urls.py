from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^tipz/', include('tipz.urls'), name='tipz'),
    url(r'^tipz/', include('tipz.urls', namespace='tipz')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
