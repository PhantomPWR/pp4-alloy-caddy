# Generated by Django 3.2.16 on 2023-03-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alloylookup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alloyelement',
            old_name='max_val',
            new_name='el_max_val',
        ),
        migrations.RenameField(
            model_name='alloyelement',
            old_name='min_val',
            new_name='el_min_val',
        ),
        migrations.RenameField(
            model_name='alloyelement',
            old_name='name',
            new_name='el_name',
        ),
        migrations.RenameField(
            model_name='alloyelement',
            old_name='symbol',
            new_name='el_symbol',
        ),
        migrations.RenameField(
            model_name='alloyelement',
            old_name='unit',
            new_name='el_unit',
        ),
        migrations.RemoveField(
            model_name='alloyelement',
            name='type',
        ),
        migrations.AddField(
            model_name='alloyelement',
            name='el_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]