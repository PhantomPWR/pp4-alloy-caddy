from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.


def account_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Remove print statement !!!
        print(username, password)
        # Remove print statement !!!

        user = authenticate(request, username=username)
        password = authenticate(request, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, "accounts/login.html")


    return render(request, "accounts/login.html", {})


def account_logout(request):
    return render(request, "accounts/logout.html", {})


def account_register(request):
    return render(request, "accounts/register.html", {})
