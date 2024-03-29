from django.urls import reverse
from django.contrib import messages
import json
from django.core import serializers
from .SendDynamic import send_welcome
from django.http import (
    HttpResponseRedirect,
    HttpResponse
    )
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
    )
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
    )
from django.contrib.auth.decorators import (
    login_required,
    permission_required
    )
from django.contrib.auth.models import (
    Group,
    Permission
    )
from .forms import (
    CreateAlloyForm,
    UpdateAlloyForm,
    CreateCategoryForm,
    UpdateCategoryForm,
    CreateSubCategoryForm,
    UpdateSubCategoryForm,
    CreateCountryForm,
    UpdateCountryForm,
    CreateFootNoteForm,
    UpdateFootNoteForm,
    RegisterUserForm
    )
from .models import (
    Country,
    Footnote,
    Subcategory,
    Category,
    Alloy
    )

# Create your views here.


@login_required(login_url='account_login')
def get_countries_list(request):
    """
    Retrieves the countries_list template.
    """
    page_title = "Alloy Countries"
    countries = Country.objects.all()
    context = {
        "page_title": page_title,
        "countries": countries
    }
    return render(
        request,
        'alloylookup/countries_list.html',
        context
        )


@login_required(login_url='account_login')
def get_footnotes_list(request):
    """
    Retrieves the footnotes_list template.
    """
    page_title = "Alloy Footnotes"
    footnotes = Footnote.objects.all()
    context = {
        "footnotes": footnotes,
        "page_title": page_title
    }
    return render(
        request,
        'alloylookup/footnotes_list.html',
        context
        )


@login_required(login_url='account_login')
def get_subcategories_list(request):
    """
    Retrieves the subcategories_list template.
    """
    page_title = "Subcategories"
    subcategories = Subcategory.objects.all().order_by('id')
    context = {
        "subcategories": subcategories,
        "page_title": page_title
    }
    return render(
        request,
        'alloylookup/subcategories_list.html',
        context
        )


@login_required(login_url='account_login')
def get_categories_list(request):
    """
    Retrieves the categories_list template.
    """
    page_title = "Alloy Categories"
    categories = Category.objects.all().order_by('id')
    context = {
        "categories": categories,
        "page_title": page_title
    }
    return render(
        request,
        'alloylookup/categories_list.html',
        context
        )


@login_required(login_url='account_login')
def get_alloy_list(request):
    """
    Retrieves the alloy_list template.
    """
    alloys = Alloy.objects.all()
    context = {
        "alloys": alloys
    }
    return render(
        request,
        'alloylookup/alloy_list.html',
        context
        )


@login_required(login_url='account_login')
def alloy_search(request):
    """
    Retrieves the alloy search results template.
    """
    alloy_details = Alloy.objects.all()  # Display all rows from Alloy model
    query = request.GET.get("search_term")  # <input name="search_term">
    alloy_object_list = Alloy.objects.search(query=query)

    context = {
        "alloy_details": alloy_details,
        "alloy_object_list": alloy_object_list
    }
    return render(
        request,
        'alloylookup/alloy_search.html',
        context
        )


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.alloy.can_add_alloy',
    login_url='account_login'
    )
def create_alloy(request):
    """
    Form for creating an alloy
    """
    create_alloy_form = CreateAlloyForm()
    page_title = "Add an Alloy"
    if request.method == "POST":
        create_alloy_form = CreateAlloyForm(request.POST)
        if create_alloy_form.is_valid():
            created_alloy = create_alloy_form.save()
            messages.success(request, "Alloy added successfully")
            return redirect(
                f'/alloy-search/?search_term={created_alloy.alloy_code}'
                )

    context = {
        'create_alloy_form': create_alloy_form,
        'page_title': page_title

    }
    return render(request, 'alloylookup/create_alloy.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.alloy.can_change_alloy',
    login_url='account_login'
    )
def update_alloy(request, pk):
    """
    Form for updating an alloy
    """

    update_alloy = get_object_or_404(Alloy, id=pk)
    update_alloy_form = UpdateAlloyForm(instance=update_alloy)

    page_title = "Update an Alloy"

    if request.method == "POST":
        update_alloy_form = UpdateAlloyForm(
            request.POST,
            instance=update_alloy
            )
        if update_alloy_form.is_valid():
            update_alloy_form.save()
            messages.success(request, "Alloy updated successfully")
            return redirect(
                '/alloy-search/?search_term={}'
                .format(update_alloy.alloy_code)
                )

    context = {
        'update_alloy_form': update_alloy_form,
        'page_title': page_title
    }

    return render(request, 'alloylookup/update_alloy.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.alloy.can_delete_alloy',
    login_url='account_login'
    )
def delete_alloy(request, pk):
    """
    Form for deleting an alloy
    """

    delete_alloy = get_object_or_404(Alloy, id=pk)
    page_title = "Delete an Alloy"

    if request.method == "POST":
        delete_alloy.delete()
        messages.success(request, "Alloy deleted")
        return redirect('/alloy-search')

    context = {
        'page_title': page_title,
        'alloy': delete_alloy
    }

    return render(request, 'alloylookup/delete_alloy.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.category.can_add_category',
    login_url='account_login'
    )
def create_category(request):
    """
    Form for creating an alloy category
    """
    create_category_form = CreateCategoryForm()
    page_title = "Add a Category"
    if request.method == "POST":
        create_category_form = CreateCategoryForm(request.POST)
        if create_category_form.is_valid():
            create_category_form.save()
            messages.success(request, "Category added successfully")
            return redirect('/categories/')

    context = {
        'create_category_form': create_category_form,
        'page_title': page_title

    }
    return render(request, 'alloylookup/create_category.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.category.can_change_category',
    login_url='account_login'
    )
def update_category(request, pk):
    """
    Form for updating an alloy category
    """

    update_category = get_object_or_404(Category, id=pk)
    update_category_form = UpdateCategoryForm(instance=update_category)

    page_title = "Update a Category"

    if request.method == "POST":
        update_category_form = UpdateCategoryForm(
            request.POST,
            instance=update_category
            )
        if update_category_form.is_valid():
            update_category_form.save()
            messages.success(request, "Category updated successfully")
            return redirect('/categories')

    context = {
        'update_category_form': update_category_form,
        'page_title': page_title
    }

    return render(request, 'alloylookup/update_category.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.category.can_delete_category',
    login_url='account_login'
    )
def delete_category(request, pk):
    """
    Form for deleting an alloy category
    """

    delete_category = get_object_or_404(Category, id=pk)
    page_title = "Delete a Category"

    if request.method == "POST":
        delete_category.delete()
        messages.success(request, "Category deleted")
        return redirect('/categories')

    context = {
        'page_title': page_title,
        'delete_category': delete_category
    }

    return render(request, 'alloylookup/delete_category.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.category.can_add_subcategory',
    login_url='account_login'
    )
def create_subcategory(request):
    """
    Form for creating an alloy subcategory
    """
    create_subcategory_form = CreateSubCategoryForm()
    page_title = "Add a Subcategory"
    if request.method == "POST":
        create_subcategory_form = CreateSubCategoryForm(request.POST)
        if create_subcategory_form.is_valid():
            create_subcategory_form.save()
            messages.success(request, "Subcategory added successfully")
            return redirect('/subcategories')

    context = {
        'create_subcategory_form': create_subcategory_form,
        'page_title': page_title

    }
    return render(request, 'alloylookup/create_subcategory.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.category.can_change_subcategory',
    login_url='account_login'
    )
def update_subcategory(request, pk):
    """
    Form for updating an alloy subcategory
    """

    update_subcategory = get_object_or_404(Subcategory, id=pk)
    update_subcategory_form = UpdateSubCategoryForm(
        instance=update_subcategory
        )

    page_title = "Update a Subcategory"

    if request.method == "POST":
        update_subcategory_form = UpdateSubCategoryForm(
            request.POST,
            instance=update_subcategory
            )
        if update_subcategory_form.is_valid():
            update_subcategory_form.save()
            messages.success(request, "Subcategory updated successfully")
            return redirect('/subcategories')

    context = {
        'update_subcategory_form': update_subcategory_form,
        'page_title': page_title
    }

    return render(request, 'alloylookup/update_subcategory.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.category.can_delete_subcategory',
    login_url='account_login'
    )
def delete_subcategory(request, pk):
    """
    Form for deleting an alloy subcategory
    """

    delete_subcategory = get_object_or_404(Subcategory, id=pk)
    page_title = "Delete a SubCategory"

    if request.method == "POST":
        delete_subcategory.delete()
        messages.success(request, "Subcategory deleted")
        return redirect('/subcategories')

    context = {
        'page_title': page_title,
        'delete_subcategory': delete_subcategory
    }

    return render(request, 'alloylookup/delete_subcategory.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.country.can_add_country',
    login_url='account_login'
    )
def create_country(request):
    """
    Form for creating a country
    """
    create_country_form = CreateCountryForm()
    page_title = "Add a Country"
    if request.method == "POST":
        create_country_form = CreateCountryForm(request.POST)
        if create_country_form.is_valid():
            create_country_form.save()
            messages.success(request, "Country added successfully")
            return redirect('/countries')

    context = {
        'create_country_form': create_country_form,
        'page_title': page_title

    }
    return render(request, 'alloylookup/create_country.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.country.can_change_country',
    login_url='account_login'
    )
def update_country(request, pk):
    """
    Form for updating a country
    """

    update_country = get_object_or_404(Country, id=pk)
    update_country_form = UpdateCountryForm(
        instance=update_country
        )

    page_title = "Update a Country"

    if request.method == "POST":
        update_country_form = UpdateCountryForm(
            request.POST,
            instance=update_country
            )
        if update_country_form.is_valid():
            update_country_form.save()
            messages.success(request, "Country updated successfully")
            return redirect('/countries')

    context = {
        'update_country_form': update_country_form,
        'page_title': page_title
    }

    return render(request, 'alloylookup/update_country.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.country.can_delete_country',
    login_url='account_login'
    )
def delete_country(request, pk):
    """
    Form for deleting a country
    """

    delete_country = get_object_or_404(Country, id=pk)
    page_title = "Delete a Country"

    if request.method == "POST":
        delete_country.delete()
        messages.success(request, "Country deleted")
        return redirect('/countries')

    context = {
        'page_title': page_title,
        'delete_country': delete_country
    }

    return render(request, 'alloylookup/delete_country.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.footnote.can_add_footnote',
    login_url='account_login'
    )
def create_footnote(request):
    """
    Form for creating a footnote
    """
    create_footnote_form = CreateFootNoteForm()
    page_title = "Add a Footnote"
    if request.method == "POST":
        create_footnote_form = CreateFootNoteForm(request.POST)
        if create_footnote_form.is_valid():
            create_footnote_form.save()
            messages.success(request, "Footnote added successfully")
            return redirect('/footnotes')

    context = {
        'create_footnote_form': create_footnote_form,
        'page_title': page_title

    }
    return render(request, 'alloylookup/create_footnote.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.footnote.can_change_footnote',
    login_url='account_login'
    )
def update_footnote(request, pk):
    """
    Form for updating a footnote
    """

    update_footnote = get_object_or_404(Footnote, id=pk)
    update_footnote_form = UpdateFootNoteForm(
        instance=update_footnote
        )

    page_title = "Update a Footnote"

    if request.method == "POST":
        update_footnote_form = UpdateFootNoteForm(
            request.POST,
            instance=update_footnote
            )
        if update_footnote_form.is_valid():
            update_footnote_form.save()
            messages.success(request, "Footnote updated successfully")
            return redirect('/footnotes')

    context = {
        'update_footnote_form': update_footnote_form,
        'page_title': page_title
    }

    return render(request, 'alloylookup/update_footnote.html', context)


@login_required(login_url='account_login')
@permission_required(
    'alloylookup.footnote.can_delete_footnote',
    login_url='account_login'
    )
def delete_footnote(request, pk):
    """
    Form for deleting a footnote
    """

    delete_footnote = get_object_or_404(Footnote, id=pk)
    page_title = "Delete a Footnote"

    if request.method == "POST":
        delete_footnote.delete()
        messages.success(request, "Footnote deleted")
        return redirect('/footnotes')

    context = {
        'page_title': page_title,
        'delete_footnote': delete_footnote
    }

    return render(request, 'alloylookup/delete_footnote.html', context)


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
            return HttpResponseRedirect(reverse('get_alloy_list'))
        else:
            messages.info(request, 'Incorrect username or password')
    context = {
        'page_title': page_title
    }

    return render(request, 'alloylookup/login.html', context)


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
            return redirect('/login')
        else:
            form = RegisterUserForm()
    context = {
        'form': form,
        'page_title': page_title
    }
    return render(request, 'alloylookup/register.html', context)


def reset_password(request):
    """
    Handles user password reset
    """
    form = ResetPasswordForm()
    page_title = 'Password Reset'
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            username = 'Password Reset'
            email = request.POST['email']
            template_id = 'd-d47a07539a314a8881f9b1f06be93cc6'

            # send welcome email via sendgrid
            send_welcome(email, username, template_id)

            # save new user
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(
                request, 'Password reset instructions sent to ' + email)
            return redirect('/login')
    context = {
        'form': form,
        'page_title': page_title
    }
    return render(request, 'alloylookup/register.html', context)
