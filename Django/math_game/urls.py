"""math_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ski_math import views

urlpatterns = [
        path("", views.home, name="home"),
        url(r'^signup/$',views.signup, name="signup"),
        url(r'^admin/',admin.site.urls),
        url(r'^skigame/$', views.skigame),
        url(r'^portal/$', views.portal),
        url(r'^stats/$', views.stats),
        url(r'^$', views.home),
        
]   

urlpatterns += staticfiles_urlpatterns()