# Generated by Django 4.2.16 on 2024-09-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_purchase_quantity_alter_product_low_stock_threshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
