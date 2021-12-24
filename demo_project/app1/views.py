from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import people,place

# Create your views here.
def fun1(request):
    obj=people.objects.all()
    obj1=place.objects.all()
    return render(request,'index.html',{'result':obj, 'result1':obj1 })
def register(request):
    if request.method =='POST':
        username=request.POST['user_name']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                print('User created')
                return redirect('login/')
        else:
            messages.info(request,'Password Not Matching!')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Password Error!')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

