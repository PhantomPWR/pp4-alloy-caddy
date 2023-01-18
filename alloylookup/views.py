from django.shortcuts import render
from .models import Country, Footnote, Subcategory, Category, AlloyDescription, Alloy

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


def get_footnotes_list(request):
    """
    Retrieves the footnotes_list template.
    """
    footnotes = Footnote.objects.all()
    context = {
        "footnotes": footnotes
    }
    return render(request, 'alloylookup/footnotes_list.html', context)


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


def get_alloy_descriptions_list(request):
    """
    Retrieves the alloy_descriptions_list template.
    """
    alloy_descriptions = AlloyDescription.objects.all()
    context = {
        "alloy_descriptions": alloy_descriptions
    }
    return render(request, 'alloylookup/alloy_descriptions_list.html', context)


def get_alloy_list(request):
    """
    Retrieves the alloy_list template.
    """
    alloys = Alloy.objects.all()
    context = {
        "alloy": alloy
    }
    return render(request, 'alloylookup/alloy_list.html', context)