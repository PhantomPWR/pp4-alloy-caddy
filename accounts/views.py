from django.shortcuts import render

# Create your views here.


def account_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

    return render(request, "accounts/login.html", {})


def account_logout(request):
    return render(request, "accounts/logout.html", {})


def account_register(request):
    return render(request, "accounts/register.html", {})
