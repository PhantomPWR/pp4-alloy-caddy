# Generated by Django 3.2.16 on 2023-03-10 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alloylookup', '0003_rename_alloy_alloyelement_alloy_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alloyelement',
            old_name='alloy_code',
            new_name='alloy',
        ),
    ]