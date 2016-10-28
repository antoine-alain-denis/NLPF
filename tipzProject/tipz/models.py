from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    creationDate = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('tipz:projectsDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'id:' + str(self.id) + ' projectName: ' + self.name + ' ' + ' owner: ' + self.owner.username

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
        return 'id: ' + str(self.id) + ' pledgeTitle: ' + self.title + ' value: ' + str(self.value) + 'EUR '\
               + ' projectName: ' + self.project.name + ' investor: ' + self.investor.username