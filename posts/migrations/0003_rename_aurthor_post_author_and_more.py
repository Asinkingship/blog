# Generated by Django 5.1 on 2024-08-14 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20240813_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='aurthor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create_on',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Status',
            new_name='status',
        ),
    ]
