from ast import Break
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'pro/home.html')

def signup(request):

    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        profile_pic=request.FILES.get('pic')

        if CustomUser.objects.filter(username=username):
            messages.warning(request, "Username already exists, try other username.")
            return redirect('signup')
        if len(username) < 10:
            messages.warning(request, "Username length should be greater than 10 charaters")
            return redirect('signup')
        if not username.isalnum():
            messages.warning(request, 'Username should be combination of alphanumeric')
            return redirect('signup')
        if CustomUser.objects.filter(email=email):
            messages.warning(request, "Email address already exists..!")
            return redirect('signup')
        if pass1 != pass2:
            messages.warning(request, "Password does not match...!")
            return redirect('signup')

        myuser=CustomUser(
            username=username,
            first_name=fname,
            last_name=lname,
            email=email,
            user_type=3,
            user_profile=profile_pic,
        )
        myuser.set_password(pass1)
        if myuser.save() != 0:
            messages.success(request, "Your account is created successfully...!")
            return redirect('signin')
            Break
        else:
            messages.warning(request, "Something went wrong, please try again..!")

    return render(request, 'pro/signup.html')


def signin(request):
    
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, 'pro/dashboard.html', {'name':fname})
        else:
            messages.error(request, "Wrong credentials, Please try again")
    return render(request, 'pro/signin.html')

def signout(request):
    logout(request)
    return redirect('home')
@login_required(login_url='/')
def dashboard(request):
    return render(request, 'pro/dashboard.html')

def change_pass(request):
    if request.method=="POST":
        user=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if CustomUser.objects.filter(username=user):
            if CustomUser.objects.filter(email=email):
                if pass1==pass2:
                    uppass=CustomUser.objects.get(username=user)
                    uppass.set_password(pass1)
                    if uppass.save() != 0:
                        messages.success(request, "Password reset successfuly!")
                        return redirect('signin')
                    else:
                        messages.error(request, "Something went wrong, Try again!")
                else:
                    messages.error(request, "Password did not matached!")
            else:
                messages.error(request, "Wrong email address, Try again")
        else:
            messages.error(request, "Wrong User name, Try again!")    

    return render(request, 'pro/change_pass.html')

def ShowUser(request):
    userList=get_user_model().objects.all()
    context={'ulist': userList}
    return render(request, 'pro/users.html', context)
