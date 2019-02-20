from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return HttpResponse("Ski Math forever!")

def skigame(request):
    return HttpResponse('Skigame')

def portal(request):
    return HttpResponse('portal')

def stats(request):
    return HttpResponse('stats')

def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})
    return HttpResponse('signup')