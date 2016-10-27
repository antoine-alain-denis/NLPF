from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=42)
    lastname = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('tipz:usersDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'id:' + str(self.id) + ' ' + self.firstname + ' ' + self.lastname

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    creationDate = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('tipz:projectsDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'id:' + str(self.id) + ' ' + self.name + ' ' + ' ' + self.owner.firstname + ' ' + self.owner.lastname

class Pledge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    value = models.PositiveIntegerField(default=1)
    project = models.ForeignKey(Project, null=False, default=0, on_delete=models.CASCADE)
    investor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('tipz:pledgesDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id) + ' ' + self.title + ' ' + str(self.value) + 'EUR '\
               + self.project.name + ' ' + self.investor.firstname + ' ' + self.investor.lastname