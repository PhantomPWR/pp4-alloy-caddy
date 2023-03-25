# Generated by Django 3.2.16 on 2023-03-25 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(unique=True)),
                ('category_name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField(unique=True)),
                ('country_name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footnote_id', models.IntegerField(unique=True)),
                ('footnote', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_id', models.IntegerField()),
                ('subcategory_name', models.CharField(max_length=300)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='category', to='alloylookup.category')),
            ],
            options={
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Alloy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alloy_code', models.IntegerField(unique=True)),
                ('alloy_description', models.CharField(max_length=300)),
                ('alloy_elements', models.JSONField(default=dict)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alloylookup.category')),
                ('country_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alloylookup.country')),
                ('primary_footnote_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_footnote_id', to='alloylookup.footnote')),
                ('secondary_footnote_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_footnote_id', to='alloylookup.footnote')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alloylookup.subcategory')),
            ],
        ),
    ]
