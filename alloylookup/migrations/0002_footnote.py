# Generated by Django 4.1.5 on 2023-01-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alloylookup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footnote_id', models.IntegerField()),
                ('footnote', models.CharField(max_length=300)),
            ],
        ),
    ]
