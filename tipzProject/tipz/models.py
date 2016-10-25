from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Owner(models.Model):
    email = models.CharField(max_length=42, primary_key=True)
    lastname = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class Investor(models.Model):
    email = models.CharField(max_length=42, primary_key=True)
    lastname = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    creationDate = models.DateTimeField(default=datetime.now, blank=True)

class Pledge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    value = models.PositiveIntegerField(default=1)