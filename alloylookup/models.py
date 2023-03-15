from django.db import models
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponse
from jsoneditor.fields.django3_jsonfield import JSONField

# Create your models here.


class Country(models.Model):
    """
    Model for Countries
    """

    class Meta:
        verbose_name_plural = "Countries"

    country_id = models.IntegerField(
        null=False,
        blank=False
    )
    country_name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.country_name)


class PrimaryFootnote(models.Model):
    """
    Model for Primary Footnotes.
    """
    footnote_id = models.IntegerField(
        null=False,
        blank=False
    )
    footnote = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.footnote)


class SecondaryFootnote(models.Model):
    """
    Model for Secondary Footnotes.
    """
    footnote_id = models.IntegerField(
        null=False,
        blank=False
    )
    footnote = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.footnote)


class Category(models.Model):
    """
    Model for Categories.
    """

    class Meta:
        verbose_name_plural = "Categories"

    category_id = models.IntegerField(
        null=False,
        blank=False
    )
    category_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    # subcategory = models.ForeignKey(
    #     Subcategory,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True
    # )

    def __str__(self):
        return str(self.category_name)


class Subcategory(models.Model):
    """
    Model for Subcategories.
    """

    class Meta:
        verbose_name_plural = "Subcategories"

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_query_name='category'
    )
    subcategory_id = models.IntegerField(
        null=False,
        blank=False
    )
    subcategory_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.subcategory_name)


class AlloyQuerySet(models.QuerySet):
    """
    Custom query set
    Used to refine alloy searches
    """
    def search(self, query=None):
        if query is None or query == "":
            return self.none()  # Return 0 results if search_term is empty
        alloy_lookup = Q(alloy_code__icontains=query) \
            | Q(alloy_description__icontains=query) \
            | Q(alloy_elements__icontains=query) \
            | Q(category__category_name__icontains=query) \
            | Q(subcategory__subcategory_name__icontains=query)

        return self.filter(alloy_lookup)


class AlloyManager(models.Manager):
    """
    Custom model manager for db lookups
    """
    def get_queryset(self):
        return AlloyQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Alloy(models.Model):
    """
    Model for Alloys.
    """
    alloy_code = models.IntegerField(
        null=False,
        blank=False,
        unique=True
    )
    country_code = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    primary_footnote_id = models.ForeignKey(
        PrimaryFootnote,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    secondary_footnote_id = models.ForeignKey(
        SecondaryFootnote,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    alloy_description = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    alloy_elements = models.JSONField(default=dict)

    objects = AlloyManager()

    def __str__(self):
        return str(self.alloy_code)
