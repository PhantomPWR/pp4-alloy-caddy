# Generated by Django 3.2.16 on 2023-02-06 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alloylookup', '0012_alter_alloy_alloy_elements_array'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alloy',
            name='alloy_elements_array',
        ),
    ]
