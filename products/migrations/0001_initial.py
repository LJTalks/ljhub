# Generated by Django 4.2.16 on 2024-09-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = False

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
