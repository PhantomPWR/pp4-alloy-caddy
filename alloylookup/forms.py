"""
ModelForms for AlloyLookup App
"""
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from django_json_widget.widgets import JSONEditorWidget
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
                'cols': '80', 'rows': '20'
                }),
            'primary_footnote_id': forms.Select(attrs={
                'class': 'form-control'
                }),
            'secondary_footnote_id': forms.Select(attrs={
                'class': 'form-control'
                }),
            'country': forms.Select(attrs={'class': 'form-control'}),
            # 'alloy_elements': forms.JSONField(attrs={'class': 'form-control'}),
        }
