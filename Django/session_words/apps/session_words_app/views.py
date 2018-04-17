# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import strftime

# Create your views here.

def index(request):
    return render(request, 'session_words_app/index.html')

def process(request):
    if not 'words' in request.session:
        request.session['words'] = []

    #make checkbox post data workable
    big = bool(request.POST.get('big'))

    #information to add
    to_add = {
        'new_word': request.POST['word'],
        'color': request.POST['color'],
        'big': big,
        'hour': strftime("%H:%M:%S %p"),
        'day': strftime("%B %d %Y"),
    }
    print big

    request.session['words'].insert(0, to_add)
    request.session.modified=True

    print request.session['words']
    return redirect('/')

def clear(request):
    request.session['words'] = []
    return redirect('/')
