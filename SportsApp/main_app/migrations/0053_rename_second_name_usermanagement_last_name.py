# Generated by Django 4.0.3 on 2022-04-08 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0052_remove_usermanagement_name_usermanagement_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermanagement',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
