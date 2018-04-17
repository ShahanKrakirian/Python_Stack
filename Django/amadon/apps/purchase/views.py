# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'purchase/index.html')

def process(request, product):
    if not 'items_ordered' in request.session:
        request.session['items_ordered'] = 0 
    if not 'total_cost' in request.session: 
        request.session['total_cost'] = 0

    # Hold cost values
    costs = {
        'shirt': 19.99,
        'sweater':29.99,
        'cup':4.99,
        'book':49.99
    }

    cost = int(request.POST['quantity']) * costs[product]
    request.session['cost'] = cost

    request.session['items_ordered'] += int(request.POST['quantity'])
    request.session['total_cost'] += cost

    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'purchase/checkout.html')

def reset(request):
    request.session.clear()
    return redirect('/amadon')