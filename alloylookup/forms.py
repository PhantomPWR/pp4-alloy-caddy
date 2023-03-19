"""
ModelForms for AlloyLookup App
"""
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from prettyjson import PrettyJSONWidget
from .models import (
    Alloy,
    Category,
    Subcategory,
    PrimaryFootnote,
    SecondaryFootnote,
    Country
    )


class CreateAlloyForm(ModelForm):
    """
    ModelForm for adding alloys
    """
    class Meta:
        """
        Meta class for CreateAlloyForm
        """
        model = Alloy
        fields = [
            'alloy_code',
            'category',
            'subcategory',
            'alloy_description',
            'primary_footnote_id',
            'secondary_footnote_id',
            'country_code',
            'alloy_elements'
            ]

        widgets = {
            'alloy_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'alloy_description': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '80', 'rows': '5'
                }),
            'primary_footnote_id': forms.Select(attrs={
                'class': 'form-control'
                }),
            'secondary_footnote_id': forms.Select(attrs={
                'class': 'form-control'
                }),
            'country_code': forms.Select(attrs={'class': 'form-control'}),
            'alloy_elements': PrettyJSONWidget(attrs={
                'initial': 'parsed',
                'class': 'form-control',
                }),
        }


class UpdateAlloyForm(ModelForm):
    """
    ModelForm for updating alloys
    """
    class Meta:
        """
        Meta class for UpdateAlloyForm
        """
        model = Alloy
        fields = [
            'id',
            'alloy_code',
            'category',
            'subcategory',
            'alloy_description',
            'primary_footnote_id',
            'secondary_footnote_id',
            'country_code',
            'alloy_elements'
            ]

        widgets = {
            'id': forms.TextInput(attrs={
                'readonly': True
            }),
            'alloy_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'alloy_description': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': '80', 'rows': '5'
                }),
            'primary_footnote_id': forms.Select(attrs={
                'class': 'form-control'
                }),
            'secondary_footnote_id': forms.Select(attrs={
                'class': 'form-control'
                }),
            'country_code': forms.Select(attrs={'class': 'form-control'}),
            'alloy_elements': PrettyJSONWidget(attrs={
                'initial': 'parsed',
                'class': 'form-control',
                }),
        }


class CreateCategoryForm(ModelForm):
    """
    ModelForm for adding alloy categories
    """
    class Meta:
        """
        Meta class for CreateCategoryForm
        """
        model = Category
        fields = [
            'category_id',
            'category_name',
            ]

        widgets = {
            'category_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
