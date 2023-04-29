import none as none
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save()
                return redirect('login')
                print("User created")
        else:
            messages.info(request,"password mismatch")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']
        user = auth.authenticate(username=uname,password=pword)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')