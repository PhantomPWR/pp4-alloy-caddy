# Generated by Django 3.2.16 on 2023-02-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alloylookup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alloy',
            name='elements',
        ),
        migrations.AddField(
            model_name='alloy',
            name='alloy_elements',
            field=models.JSONField(default='{}'),
        ),
    ]
