# Generated by Django 4.0.3 on 2022-04-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0062_rename_phonenumber_usermanagement_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanagement',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
    ]
