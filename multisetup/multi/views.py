from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

#first signup, login and logout function
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# first section end

# Create your views here.
def home(request):
    return render(request, 'multi/home.html')

def signin(request):
    
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, 'multi/dashboard.html', {'name':fname})
        else:
            messages.error(request, "Wrong credentials, Please try again")
    return render(request, 'multi/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You logout successfully!")
    return redirect('home')

def signup(request):
    
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exits, Please try other username")
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request, "This email address already exits, Please try another email")
            return redirect('signup')

        if len(username) < 10:
            messages.error(request, "Username length should be greater than 10 characters")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Password does not match!, try again")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username should contain alphanumeric!")
            return redirect('signup')
        
        createuser=User.objects.create_user(username, email, pass1)
        createuser.first_name=fname
        createuser.last_name=lname
        createuser.save()

        #createuser=User(
         #   username=username,
          #  first_name=fname,
           # last_name=lname,
            # email=email,
            # password=pass1,
        #)
        
        messages.success(request, "User created successfuly, Login!")
        return redirect('signin')


    return render(request, 'multi/signup.html')

