from django.db import models
from django.conf import settings

# Create your models here.


class Country(models.Model):
    """
    Model for Countries.
    """
    country_id = models.IntegerField(null=False, blank=False)
    country_name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return str(self.country_name)


class Footnote(models.Model):
    """
    Model for Footnotes.
    """
    footnote_id = models.IntegerField(null=False, blank=False)
    footnote = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return str(self.footnote)