from django.urls import reverse
import json
from django.core import serializers
from django.http import (
    HttpResponseRedirect,
    HttpResponse
    )
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
    )
from django.contrib import messages
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
from .forms import (
    CreateAlloyForm,
    UpdateAlloyForm,
    CreateCategoryForm,
    UpdateCategoryForm
    )
from .models import (
    Country,
    PrimaryFootnote,
    SecondaryFootnote,
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
    countries = Country.objects.all()
    context = {
        "countries": countries
    }
    return render(
        request,
        'alloylookup/countries_list.html',
        context
        )


@login_required(login_url='account_login')
def get_primary_footnotes_list(request):
    """
    Retrieves the primary_footnotes_list template.
    """
    primary_footnotes = PrimaryFootnote.objects.all()
    context = {
        "primary_footnotes": primary_footnotes
    }
    return render(
        request,
        'alloylookup/primary_footnotes_list.html',
        context
        )


@login_required(login_url='account_login')
def get_secondary_footnotes_list(request):
    """
    Retrieves the secondary_footnotes_list template.
    """
    secondary_footnotes = SecondaryFootnote.objects.all()
    context = {
        "secondary_footnotes": secondary_footnotes
    }
    return render(
        request,
        'alloylookup/secondary_footnotes_list.html',
        context
        )


@login_required(login_url='account_login')
def get_subcategories_list(request):
    """
    Retrieves the subcategories_list template.
    """
    subcategories = Subcategory.objects.all().order_by('id')
    context = {
        "subcategories": subcategories
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
            create_alloy_form.save()
            messages.success(request, "Alloy added successfully")
            # return redirect(
            #     '/alloy_search/?search_term={}'
            #     .format(create_alloy_form.alloy_code)
            #     )
            return redirect('/alloy_search')

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
                '/alloy_search/?search_term={}'
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
        return redirect('/alloy_search')

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
            return redirect('/categories')

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
    'alloylookup.alloy.can_delete_alloy',
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