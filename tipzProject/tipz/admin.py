from django.contrib import admin
from tipz.models import User
from tipz.models import Project
from tipz.models import Pledge

# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Pledge)
