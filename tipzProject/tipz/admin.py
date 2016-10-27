from django.contrib import admin
from tipz.models import Pledge
from tipz.models import Project
from tipz.models import User


# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Pledge)
