# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from website.forms import LoginForm

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "admin.html",{})

def trylog(request):
    if request.POST:
        LoginDetails=LoginForm(request.POST)
        if LoginDetails.is_valid():
            userid=LoginDetails.cleaned_data['userid']
            request.session['userid']=userid
            return render(request, "dash.html", {})
        else:
            return render(request,"admin.html",{"message":"Invalid Email or Password","color":"red"})
    else:
        return render(request,"admin.html",{"message":"Sorry. We encountered an error!","color":"red"})

