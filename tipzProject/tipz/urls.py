from django.conf.urls import url
from tipz import views

urlpatterns = [
    # /tipz/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /tipz/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /tipz/users/
    url(r'^users/$', views.UsersView.as_view(), name='users'),
    # /tipz/projects/
    url(r'^projects/$', views.ProjectsView.as_view(), name='projects'),
    # /tipz/pledges/
    url(r'^pledges/$', views.PledgesView.as_view(), name='pledges'),

    # /tipz/users/1/
    url(r'^users/(?P<pk>[0-9]+)/$', views.UsersDetailView.as_view(), name='usersDetail'),
    # /tipz/projects/1/
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectsDetailView.as_view(), name='projectsDetail'),
    # /tipz/pledges/1/
    url(r'^pledges/(?P<pk>[0-9]+)/$', views.PledgesDetailView.as_view(), name='pledgesDetail'),

    # /tipz/users/add/
    url(r'^users/add/$', views.UserCreate.as_view(), name='users-add'),
    # /tipz/projects/add/
    url(r'^projects/add/$', views.ProjectCreate.as_view(), name='projects-add'),
    # /tipz/pledges/add/
    url(r'^pledges/add/$', views.PledgeCreate.as_view(), name='pledges-add'),

    # /tipz/users/1/edit/
    url(r'^users/(?P<pk>[0-9]+)/edit/$', views.UserUpdate.as_view(), name='users-update'),
    # /tipz/projects/1/edit/
    url(r'^projects/(?P<pk>[0-9]+)/edit/$', views.ProjectUpdate.as_view(), name='projects-update'),
    # /tipz/pledges/1/edit/
    url(r'^pledges/(?P<pk>[0-9]+)/edit/$', views.PledgeUpdate.as_view(), name='pledges-update'),

    # /tipz/projects/1/delete/
    url(r'^projects/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='projects-delete'),
    # /tipz/pledges/1/delete/
    url(r'^pledges/(?P<pk>[0-9]+)/delete/$', views.PledgeDelete.as_view(), name='pledges-delete')]