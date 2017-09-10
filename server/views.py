from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def key_api(request):
    username=request.session.get('user','')
    
    return render(request, 'key_api.html' )
