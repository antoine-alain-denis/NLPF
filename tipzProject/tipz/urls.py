from django.conf.urls import url
from tipz import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
