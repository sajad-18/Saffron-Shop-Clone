# Generated by Django 5.0.1 on 2025-03-05 09:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_feature_products_image2_products_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='feature',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
