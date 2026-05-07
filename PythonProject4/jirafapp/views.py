from pydoc import Doc, HTMLDoc

from django.core.files import temp
from django.http import HttpResponse
from django.shortcuts import render

def function1(request):
    return render(request,'zuzu.html')
def function2(request):
    return render(request,'first.html')
def function3(request):
    return render (request,'jaja.html')

