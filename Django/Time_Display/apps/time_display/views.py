# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
    "Day": strftime("%b %d, %Y", gmtime()), 
    "Hour": strftime("%H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', context)
