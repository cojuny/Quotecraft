from django.http import HttpResponse 
from django.shortcuts import render 

def request_webpage(request): 
    return render(request, 'index.html') 