from itertools import product

from django.shortcuts import render, redirect

from hello_app.forms import ProductForm
from hello_app.models import Product


# Create your views here.
def index(request):
    return render(request,'index.html')

def add_product(request):
    form=ProductForm()
    if  request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('function2')

    return render(request,'add_product.html',{'form':form})

def product_read(request):
    data=Product.objects.all()
    return render(request,'product_read.html',{'data':data})


def product_edit(request,id):
    data=Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('function3')
    else:
        form = ProductForm(instance=data)
        return render(request,'product_edit.html',{'form':form})

def product_delete(request, id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('function3')


