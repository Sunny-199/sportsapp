# Generated by Django 4.0.3 on 2022-04-18 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0061_rename_first_name_usermanagement_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermanagement',
            old_name='phonenumber',
            new_name='phoneno',
        ),
    ]
