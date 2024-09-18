# Generated by Django 4.2.16 on 2024-09-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='low_stock_threshold',
            field=models.PositiveIntegerField(default=10),
        ),
    ]