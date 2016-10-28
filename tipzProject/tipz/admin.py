from django.contrib import admin
from tipz.models import Pledge
from tipz.models import Project
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Project)
admin.site.register(Pledge)
