from django.http import HttpResponse
from django.http import HttpResponse
from django.views import View

def home(request):
    return HttpResponse("Ski Math forever!")

def skigame(request):
    return HttpResponse('skigame')

def portal(request):
    return HttpResponse('portal')

def stats(request):
    return HttpResponse('stats')