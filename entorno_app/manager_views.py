from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request,'manager/home.html')

@login_required(login_url='/')
def addData(request):
    return render(request,'manager/add_data.html')

@login_required(login_url='/')

def RESOURCES(request):
    
    return render(request,'manager/resources.html')

@login_required(login_url='/')

def viewData(request):
    return render(request,'manager/view_data.html')
