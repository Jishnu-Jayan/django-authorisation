from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Application
# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                print('User created')
                return redirect('login')
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
            messages.info(request,'Username or Password Error!')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'home.html')

def application(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        gender=request.POST['gender']
        age=request.POST['age']
        phone=request.POST['phone']
        dob=request.POST['dob']
        district=request.POST['district']
        branch=request.POST['branch']
        acc_type=request.POST['account_type']
        address=request.POST['address']
        address_full=request.POST['address_full']
        zip=request.POST['zip']

        if Application.objects.filter(name=name).exists():
            messages.info(request, 'This name already registered')
            return redirect('application')
        else:
            application = Application(name=name,email=email,gender=gender,age=age,phone=phone,dob=dob,district=district,branch=branch,acc_type=acc_type,address=address,address_full=address_full,zip=zip)
            application.save()
            messages.info(request,'Successfully Submitted')
            return redirect('application')



    return render(request,'application.html')