from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x = 1
    y = 2
    return x+y

def sayhello(request):
    #return HttpResponse("Hello World!")
    x = calculate()
    y = 2
    return render(request, "hello.html", {'name': "Vedang"})