from django.conf.urls import url
from tipz import views

urlpatterns = [
    # /tipz/
    url(r'^$', views.index, name='index'),
    # /tipz/1/
    url(r'^(?P<UsersId>[0-9]+)/$', views.detail, name='detail'),
]