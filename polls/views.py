from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World, you're at the poll index MATE.")

# Create your views here.
