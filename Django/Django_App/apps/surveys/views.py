# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def surveys(request):
    message = 'placeholder to display all the surveys created'
    return HttpResponse(message)

def surveys_new(request):
    message = 'placeholder for users to add new survey'
    return HttpResponse(message)

