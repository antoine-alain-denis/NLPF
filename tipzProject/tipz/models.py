from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class User(models.Model):
    id = models.AutoField(default=1, primary_key=True)
    email = models.CharField(max_length=42)
    lastname = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id) + ' ' + self.firstname + ' ' + self.lastname

class Project(models.Model):
    id = models.AutoField(default=1, primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    creationDate = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

class Pledge(models.Model):
    id = models.AutoField(default=1, primary_key=True)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    value = models.PositiveIntegerField(default=1)
    investor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)