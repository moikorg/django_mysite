from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #actualData =
    return HttpResponse('<h1>Sonnen View homepage</h1>')