from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def home(request):
    return HttpResponse("Ski Math forever!")

def skigame(request):
    return HttpResponse('Skigame')

def portal(request):
    return HttpResponse('portal')

def stats(request):
    return HttpResponse('stats')