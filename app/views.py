from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def exemplo(request):
    msg = "<h1>Hello World!</h1>"

    return HttpResponse(msg)