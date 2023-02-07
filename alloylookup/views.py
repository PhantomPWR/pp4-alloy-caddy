from django.shortcuts import render
from .models import Country, PrimaryFootnote, SecondaryFootnote, Subcategory, Category, Alloy

# Create your views here.


def get_countries_list(request):
    """
    Retrieves the countries_list template.
    """
    countries = Country.objects.all()
    context = {
        "countries": countries
    }
    return render(request, 'alloylookup/countries_list.html', context)


def get_primary_footnotes_list(request):
    """
    Retrieves the primary_footnotes_list template.
    """
    primary_footnotes = PrimaryFootnote.objects.all()
    context = {
        "primary_footnotes": primary_footnotes
    }
    return render(request, 'alloylookup/primary_footnotes_list.html', context)


def get_secondary_footnotes_list(request):
    """
    Retrieves the secondary_footnotes_list template.
    """
    secondary_footnotes = SecondaryFootnote.objects.all()
    context = {
        "secondary_footnotes": secondary_footnotes
    }
    return render(request, 'alloylookup/secondary_footnotes_list.html', context)


def get_subcategories_list(request):
    """
    Retrieves the subcategories_list template.
    """
    subcategories = Subcategory.objects.all()
    context = {
        "subcategories": subcategories
    }
    return render(request, 'alloylookup/subcategories_list.html', context)


def get_categories_list(request):
    """
    Retrieves the categories_list template.
    """
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'alloylookup/categories_list.html', context)


def get_alloy_list(request):
    """
    Retrieves the alloy_list template.
    """
    alloys = Alloy.objects.all()
    context = {
        "alloys": alloys
    }
    return render(request, 'alloylookup/alloy_list.html', context)


def alloy_search(request):
    """
    Retrieves the alloy search results template.
    """
    alloy_details = Alloy.objects.all()  # Display all rows from the Alloy model

    context = {
        "alloy_details": alloy_details
    }
    return render(request, 'alloylookup/alloy_search.html', context)