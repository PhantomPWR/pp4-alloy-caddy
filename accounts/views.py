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
from django.contrib.auth.models import (
    Group,
    Permission
    )
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
    )
from .SendDynamic import send_welcome
from .forms import RegisterUserForm

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

    return render(request, 'accounts/login.html', context)


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
    form = RegisterUserForm()
    page_title = 'Account Registration'
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            username = request.POST['username']
            template_id = 'd-d47a07539a314a8881f9b1f06be93cc6'

            # send welcome email using sendgrid
            send_welcome(email, username, template_id)

            # assign new user to correct usergroup
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name='User')
            user.groups.add(user_group)
            permission = Permission.objects.get(name='Can view alloy')
            user.user_permissions.add(permission)

            # save new user
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('alloy_search')
        else:
            form = RegisterUserForm()
    context = {
        'form': form,
        'page_title': page_title
    }
    return render(request, 'accounts/register.html', context)
