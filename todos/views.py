from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Todo


class HomePageView(ListView):
    model = Todo
    template_name = 'home.html'
