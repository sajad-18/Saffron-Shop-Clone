# Generated by Django 5.0.1 on 2025-02-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='feature',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/'),
        ),
    ]
