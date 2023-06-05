from django.http import HttpResponse
# se importa HTTPRESPONSE
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hola, desde mi primera vista")
def author(request):
    return HttpResponse("Author: Gael Gaona🤯")
