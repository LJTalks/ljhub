# Generated by Django 4.2.16 on 2024-10-02 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='limit_one_per_customer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='low_stock_alert_sent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='low_stock_threshold',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tier_one_limit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tier_one_price',
        ),
    ]