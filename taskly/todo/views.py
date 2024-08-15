from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    context = {
        'name': 'Taskly',
    }

    return render(request, 'index.html', context=context)

def register(request):
   return render(request, 'register.html')


def my_login(request):
   return render(request, 'login.html')


