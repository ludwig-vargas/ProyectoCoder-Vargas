# Generated by Django 4.1.3 on 2022-11-11 01:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('code_product', models.IntegerField()),
                ('category', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]