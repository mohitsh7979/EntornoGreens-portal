from django.shortcuts import render,redirect,HttpResponse
from main_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def doLogout(request):
    logout(request)
    return redirect('login')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),) 
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('manager_home')
            elif user_type == "2":
                return HttpResponse('This is Employee Panel of Entorno Greens')
            else:
                messages.error(request,'Email or Password is Invalid!')
                return redirect('login')
        
        else:
            messages.error(request,'Email or Password is Invalid!')

            return redirect('login')

def PROFILE(request):
    
    return render(request, 'profile.html')

def EVENTS(request):
    
    return render(request, 'event_create.html')


def REGISTER(request):
    
    return render(request, 'register.html')