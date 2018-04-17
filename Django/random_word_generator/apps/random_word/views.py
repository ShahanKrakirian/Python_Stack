# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not 'attempt_number' in request.session:
        request.session['attempt_number'] = 1
    else: 
        request.session['attempt_number'] += 1

    info = {
        'random_word': get_random_string(14)
    }

    return render(request, 'random_word/index.html', info)

def reset(request):
    del request.session['attempt_number'] 
    return redirect('/')

