from django.shortcuts import render
from .models import Country, Footnote

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
