# Generated by Django 3.2.16 on 2023-02-11 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alloylookup', '0014_auto_20230206_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='category', to='alloylookup.category'),
        ),
    ]