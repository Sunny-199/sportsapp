# Generated by Django 4.0.3 on 2022-04-18 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0065_rename_coachname_coachmanagement_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coachmanagement',
            old_name='sportscenter',
            new_name='sportcenter',
        ),
    ]
