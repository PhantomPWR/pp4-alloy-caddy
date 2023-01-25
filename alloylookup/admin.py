from django.contrib import admin
from .models import Country, PrimaryFootnote, SecondaryFootnote, Subcategory, Category, Alloy

# Register your models here.

admin.site.register(Country)
admin.site.register(PrimaryFootnote)
admin.site.register(SecondaryFootnote)
admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Alloy)
