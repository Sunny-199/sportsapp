# Generated by Django 4.0.3 on 2022-04-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0050_rename_sportscenter_categories_sports_center_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='username',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='transcations',
            old_name='username',
            new_name='user_name',
        ),
    ]
