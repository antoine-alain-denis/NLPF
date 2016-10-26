from django.conf.urls import url
from tipz import views

urlpatterns = [
    # /tipz/
    url(r'^$', views.index, name='index'),

    # /tipz/users/
    url(r'^users/$', views.users, name='users'),
    # /tipz/projects/
    url(r'^projects/$', views.projects, name='projects'),
    # /tipz/pledges/
    url(r'^pledges/$', views.pledges, name='pledges'),

    # /tipz/users/1/
    url(r'^users/(?P<userId>[0-9]+)/$', views.usersDetail, name='usersDetail'),
    # /tipz/projects/1/
    url(r'^projects/(?P<projectId>[0-9]+)/$', views.projectsDetail, name='projectsDetail'),
    # /tipz/pledges/1/
    url(r'^pledges/(?P<pledgeId>[0-9]+)/$', views.pledgesDetail, name='pledgesDetail'),
]