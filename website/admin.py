# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Event
from .models import Admin
from .models import User

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Admin)