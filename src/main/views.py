from django.urls import reverse
from django.shortcuts import render, redirect
from .models import get_quote, insert_quote


def request_webpage(request): 
    context = get_quote(request.GET.get('sort'))
    return render(request, 'index.html', context) 

def create_quote(request):
    if request.method == 'POST':
        quote = request.POST.get('quote')
        author = request.POST.get('author')
        insert_quote(quote, author)
    
    return redirect(request_webpage)

def latest(request):
    return render(request, 'latest.html')