from django.forms import Form
from django.shortcuts import render, redirect

from redapp.forms import StudentForm, CollegeForm
from redapp.models import Student, College


# Create your views here.
def function1(request):
    form = StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fun1')
    return render(request,'index.html',{'form':form})
def function2(request):
    data=Student.objects.all()
    return render(request,'table.html',{'data':data})
def function3(request,id):
    data=Student.objects.get(id=id)
    form=StudentForm(instance=data)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('fun2')
    return render(request,'update.html',{'form':form})
def function4(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('fun2')
def function5(request):
    form=CollegeForm()
    return render(request,'college_main.html',{'form':form})