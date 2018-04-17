# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    return render(request, 'game/index.html')

def process(request, location):

    #initialize total
    if not 'total' in request.session:
        request.session['total'] = 0
    if not 'phrase' in request.session:
        request.session['phrase'] = []
    if not 'class' in request.session: 
        request.session['class'] = []

    #handle different inputs 
    if location == 'farm':
        addme = random.randrange(10,21)
        request.session['phrase'].insert(0, ("You harvested " + str(addme) + " gold!", 'green'))
        request.session['total'] += addme
    if location == 'cave':
        addme = random.randrange(5,11)
        request.session['phrase'].insert(0, ("You dug up " + str(addme) + " gold!", 'green'))
        request.session['total'] += addme
    if location == 'house':
        addme = random.randrange(2,6)
        request.session['phrase'].insert(0, ("You asked your grandmother for " + str(addme) + " gold!", 'green'))
        request.session['total'] += addme
    if location == 'casino':
        addme = random.randrange(-50,51)
        if addme >= 0:
            request.session['phrase'].insert(0, ("You got lucky this time. " + str(addme) + " gold!", 'green'))
            request.session['total'] += addme
        else: 
            request.session['phrase'].insert(0, (str(addme) + " gold. Maybe you can win it back...", 'red'))
            request.session['total'] += addme 
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')