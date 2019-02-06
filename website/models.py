# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=30)
    amt=models.IntegerField()

class Admin(models.Model):
    userid=models.CharField(max_length=15)
    password=models.CharField(max_length=20)

class User(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phno=models.PositiveIntegerField()
    institute=models.CharField(max_length=70)
    regid=models.CharField(max_length=10)
    events=models.ManyToManyField(Event)
    toPay=models.IntegerField()
    PaidAmt=models.IntegerField()
    lastEdit=models.ForeignKey(Admin)
    


