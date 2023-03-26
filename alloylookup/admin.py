from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import (
    Country,
    Footnote,
    Subcategory,
    Category,
    Alloy,
    User
    )

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country_name')
    ordering = ['country_id']


class FootNoteAdmin(admin.ModelAdmin):
    list_display = ('footnote_id', 'footnote')
    ordering = ['footnote_id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'category_name')
    ordering = ['id']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory_id', 'subcategory_name')
    ordering = ['subcategory_id']


class AlloyAdmin(admin.ModelAdmin):
    list_display = ('id', 'alloy_code', 'alloy_description')
    ordering = ['alloy_code']
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(Country, CountryAdmin)
admin.site.register(Footnote, FootNoteAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Alloy, AlloyAdmin)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Register User Admin
    """
    pass
