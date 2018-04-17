# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def users(request):
    message = 'placeholder to later display all the list of users'
    return HttpResponse(message)

def register(request):
    message = 'placeholder for register page'
    return HttpResponse(message)

def login(request):
    message = 'placeholder for users to login'
    return HttpResponse(message)