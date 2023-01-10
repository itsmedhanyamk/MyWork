from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']
        user = auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        if pswd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pswd)
                user.save()
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"Password not matched")
            print("Password not match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')