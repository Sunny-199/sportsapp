# Generated by Django 4.0.3 on 2022-04-18 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0067_rename_sports_center_categories_sportscenter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='sportscenter',
            new_name='sportcenter',
        ),
    ]
