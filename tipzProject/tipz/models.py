from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class User(models.Model):
    email = models.CharField(max_length=42, primary_key=True)
    lastname = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.lastname + ' ' + self.firstname

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    creationDate = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class Pledge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    value = models.PositiveIntegerField(default=1)
    investor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)