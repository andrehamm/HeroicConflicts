from django.urls import path

from ski_math import views

urlpatterns = [
        path("", views.home, name="home"),
]   