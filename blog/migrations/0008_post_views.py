# Generated by Django 4.2.16 on 2024-09-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_content_comment_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
