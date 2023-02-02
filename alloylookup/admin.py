from django.contrib import admin
from .models import Country, PrimaryFootnote, SecondaryFootnote, Subcategory, Category, Alloy

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    ordering = ['category_id']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_id', 'subcategory_name')
    ordering = ['subcategory_id']


class AlloyAdmin(admin.ModelAdmin):
    list_display = ('alloy_code', 'alloy_description')
    ordering = ['alloy_code']


admin.site.register(Country)
admin.site.register(PrimaryFootnote)
admin.site.register(SecondaryFootnote)
admin.site.register(Subcategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Alloy, AlloyAdmin)
