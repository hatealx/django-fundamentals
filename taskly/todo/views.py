from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    clientList = [
       {
          "id":1,
          "name": "George",
          "profession" :"web developer"
          
       },
       {
           "id":2,
          "name": "Mike",
          "profession" :"Architect"
       },
       {
          "id":3,
          "name": "abel",
          "profession" :"Data scientist"
       }
    ]
    context = {"client": clientList}

    return render(request, 'index.html', context=context)

def register(request):
   return render(request, 'register.html')


def my_login(request):
   return render(request, 'login.html')


