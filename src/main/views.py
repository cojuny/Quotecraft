from django.http import HttpResponse 
from django.shortcuts import render 
from .models import get_quote


def request_webpage(request): 
    quotes = get_quote()
    context = {'quotes': quotes}
    return render(request, 'index.html', context) 

