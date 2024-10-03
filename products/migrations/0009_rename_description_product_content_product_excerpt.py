# Generated by Django 4.2.16 on 2024-10-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_related_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='product',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
