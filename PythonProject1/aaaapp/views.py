from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def functions1(request):
    return render(request,'index.html')
def functions2(request):
    return render(request,"first.html")
