# Generated by Django 4.2.16 on 2024-09-27 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_updated_on_alter_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='commenter',
        ),
    ]
