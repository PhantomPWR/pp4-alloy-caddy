from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
    )
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
    )

# Create your views here.


def account_login(request):
    """
    Handle user login
    """
    page_title = 'Account Login'
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('alloy_search'))
        else:
            messages.info(request, 'Incorrect username or password')
    context = {
        'page_title': page_title
    }

    return render(request, "accounts/login.html", context)


def account_logout(request):
    """
    Handle user logging out
    """
    logout(request)
    return HttpResponseRedirect(reverse('account_login'))


def account_register(request):
    """
    Handle user account registration
    """
    page_title = 'Account Registration'

    context = {
        'page_title': page_title
    }

    return render(request, "accounts/register.html", context)
