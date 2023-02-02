from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField

# Create your models here.


class Country(models.Model):
    """
    Model for Countries.
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
    Model for Sub-categories.
    """

    class Meta:
        verbose_name_plural = "Subcategories"

    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    #     related_query_name='category'
    # )
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

    ELEMENT_CHOICES = (
        ('si', 'Si'),
        ('fe', 'Fe'),
        ('cu', 'Cu')
    )

    # elements = ArrayField(
    #     models.CharField(max_length=255),
    #     default=[],
    #     blank=True,
    #     choices=ELEMENT_CHOICES
    #     )
    elements = MultiSelectField(
        max_length=255,
        choices=ELEMENT_CHOICES
    )

 # Elements
    si_min = models.CharField(max_length=300, null=True, blank=True)
    si_max = models.CharField(max_length=300, null=True, blank=True)
    fe_min = models.CharField(max_length=300, null=True, blank=True)
    fe_max = models.CharField(max_length=300, null=True, blank=True)
    cu_min = models.CharField(max_length=300, null=True, blank=True)
    cu_max = models.CharField(max_length=300, null=True, blank=True)
    mn_min = models.CharField(max_length=300, null=True, blank=True)
    mn_max = models.CharField(max_length=300, null=True, blank=True)
    mg_min = models.CharField(max_length=300, null=True, blank=True)
    mg_max = models.CharField(max_length=300, null=True, blank=True)
    cr_min = models.CharField(max_length=300, null=True, blank=True)
    cr_max = models.CharField(max_length=300, null=True, blank=True)
    ni_min = models.CharField(max_length=300, null=True, blank=True)
    ni_max = models.CharField(max_length=300, null=True, blank=True)
    zn_min = models.CharField(max_length=300, null=True, blank=True)
    zn_max = models.CharField(max_length=300, null=True, blank=True)
    ti_min = models.CharField(max_length=300, null=True, blank=True)
    ti_max = models.CharField(max_length=300, null=True, blank=True)
    ga_min = models.CharField(max_length=300, null=True, blank=True)
    ga_max = models.CharField(max_length=300, null=True, blank=True)
    v_min = models.CharField(max_length=300, null=True, blank=True)
    v_max = models.CharField(max_length=300, null=True, blank=True)
    mo_min = models.CharField(max_length=300, null=True, blank=True)
    mo_max = models.CharField(max_length=300, null=True, blank=True)
    c_min = models.CharField(max_length=300, null=True, blank=True)
    c_max = models.CharField(max_length=300, null=True, blank=True)
    al_min = models.CharField(max_length=300, null=True, blank=True)
    al_max = models.CharField(max_length=300, null=True, blank=True)
    cb_min = models.CharField(max_length=300, null=True, blank=True)
    cb_max = models.CharField(max_length=300, null=True, blank=True)
    co_min = models.CharField(max_length=300, null=True, blank=True)
    co_max = models.CharField(max_length=300, null=True, blank=True)
    w_min = models.CharField(max_length=300, null=True, blank=True)
    w_max = models.CharField(max_length=300, null=True, blank=True)
    zr_min = models.CharField(max_length=300, null=True, blank=True)
    zr_max = models.CharField(max_length=300, null=True, blank=True)
    ag_min = models.CharField(max_length=300, null=True, blank=True)
    ag_max = models.CharField(max_length=300, null=True, blank=True)
    s_min = models.CharField(max_length=300, null=True, blank=True)
    s_max = models.CharField(max_length=300, null=True, blank=True)
    be_min = models.CharField(max_length=300, null=True, blank=True)
    be_max = models.CharField(max_length=300, null=True, blank=True)
    ta_min = models.CharField(max_length=300, null=True, blank=True)
    ta_max = models.CharField(max_length=300, null=True, blank=True)
    sn_min = models.CharField(max_length=300, null=True, blank=True)
    sn_max = models.CharField(max_length=300, null=True, blank=True)
    re_min = models.CharField(max_length=300, null=True, blank=True)
    re_max = models.CharField(max_length=300, null=True, blank=True)
    bi_min = models.CharField(max_length=300, null=True, blank=True)
    bi_max = models.CharField(max_length=300, null=True, blank=True)
    b_min = models.CharField(max_length=300, null=True, blank=True)
    b_max = models.CharField(max_length=300, null=True, blank=True)
    o_min = models.CharField(max_length=300, null=True, blank=True)
    o_max = models.CharField(max_length=300, null=True, blank=True)
    as_min = models.CharField(max_length=300, null=True, blank=True)
    as_max = models.CharField(max_length=300, null=True, blank=True)
    li_min = models.CharField(max_length=300, null=True, blank=True)
    li_max = models.CharField(max_length=300, null=True, blank=True)
    ca_min = models.CharField(max_length=300, null=True, blank=True)
    ca_max = models.CharField(max_length=300, null=True, blank=True)
    cd_min = models.CharField(max_length=300, null=True, blank=True)
    cd_max = models.CharField(max_length=300, null=True, blank=True)
    ce_min = models.CharField(max_length=300, null=True, blank=True)
    ce_max = models.CharField(max_length=300, null=True, blank=True)
    h_min = models.CharField(max_length=300, null=True, blank=True)
    h_max = models.CharField(max_length=300, null=True, blank=True)
    hf_min = models.CharField(max_length=300, null=True, blank=True)
    hf_max = models.CharField(max_length=300, null=True, blank=True)
    la_min = models.CharField(max_length=300, null=True, blank=True)
    la_max = models.CharField(max_length=300, null=True, blank=True)
    n_min = models.CharField(max_length=300, null=True, blank=True)
    n_max = models.CharField(max_length=300, null=True, blank=True)
    nb_min = models.CharField(max_length=300, null=True, blank=True)
    nb_max = models.CharField(max_length=300, null=True, blank=True)
    sb_min = models.CharField(max_length=300, null=True, blank=True)
    sb_max = models.CharField(max_length=300, null=True, blank=True)
    se_min = models.CharField(max_length=300, null=True, blank=True)
    se_max = models.CharField(max_length=300, null=True, blank=True)
    sr_min = models.CharField(max_length=300, null=True, blank=True)
    sr_max = models.CharField(max_length=300, null=True, blank=True)
    su_min = models.CharField(max_length=300, null=True, blank=True)
    su_max = models.CharField(max_length=300, null=True, blank=True)
    rr_min = models.CharField(max_length=300, null=True, blank=True)
    rr_max = models.CharField(max_length=300, null=True, blank=True)
    te_min = models.CharField(max_length=300, null=True, blank=True)
    te_max = models.CharField(max_length=300, null=True, blank=True)
    y_min = models.CharField(max_length=300, null=True, blank=True)
    y_max = models.CharField(max_length=300, null=True, blank=True)
    ru_min = models.CharField(max_length=300, null=True, blank=True)
    ru_max = models.CharField(max_length=300, null=True, blank=True)
    pb_min = models.CharField(max_length=300, null=True, blank=True)
    pb_max = models.CharField(max_length=300, null=True, blank=True)
    p_min = models.CharField(max_length=300, null=True, blank=True)
    p_max = models.CharField(max_length=300, null=True, blank=True)

    # Compounds
    wc_min = models.CharField(max_length=300, null=True, blank=True)
    wc_max = models.CharField(max_length=300, null=True, blank=True)
    n2_min = models.CharField(max_length=300, null=True, blank=True)
    n2_max = models.CharField(max_length=300, null=True, blank=True)
    tac_min = models.CharField(max_length=300, null=True, blank=True)
    tac_max = models.CharField(max_length=300, null=True, blank=True)
    th02_min = models.CharField(max_length=300, null=True, blank=True)
    th02_max = models.CharField(max_length=300, null=True, blank=True)
    tic_min = models.CharField(max_length=300, null=True, blank=True)
    tic_max = models.CharField(max_length=300, null=True, blank=True)
    so_min = models.CharField(max_length=300, null=True, blank=True)
    so_max = models.CharField(max_length=300, null=True, blank=True)

    others_each = models.CharField(max_length=300, null=True, blank=True)
    others_total = models.CharField(max_length=300, null=True, blank=True)
    special_note = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return str(self.alloy_code)
