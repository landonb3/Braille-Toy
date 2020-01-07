from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# attempts to authenticate and login the user
def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            return render(request, 'splash.html', {"error": "Incorrect username or password"})
    return render(request, 'splash.html', {})

# attempts to create the user object, with error checking
def signup_view(request):
    if request.method == "POST":
        try:
            if len(request.POST['username']) is 0:
                return render(request, 'signup.html', {"error": "Please enter a username"})
            if len(request.POST['email']) is 0:
                return render(request, 'signup.html', {"error": "Please enter an email"})
            if len(request.POST['password']) is 0:
                return render(request, 'signup.html', {"error": "Please enter a password"})
            if len(request.POST['name']) is 0:
                return render(request, 'signup.html', {"error": "Please enter what you'd like to be called"})
            if User.objects.filter(email=request.POST['email']).exists():
                return render(request, 'signup.html', {"error": "Email already taken"})
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'signup.html', {"error": "Username already taken"})
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'],first_name=request.POST['name'],last_name='0')
            login(request, user)
            return redirect("/home")
        except:
            return render(request, 'signup.html', {"error": "Please correctly fill out all required fields"})
    return render(request, 'signup.html', {})

# logs out user
def logout_view(request):
    logout(request)
    return redirect("/")

def splash_view(request):
    return render(request, 'splash.html', {})