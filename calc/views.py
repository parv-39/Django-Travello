from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'Parv'})

def add(request):

    val1 = int(request.POST.get('num1'))
    val2 = int(request.POST.get('num2'))
    res1 = val1 + val2

    return render(request, 'result.html',{'result': res1})
