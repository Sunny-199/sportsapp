# Generated by Django 4.0.3 on 2022-04-21 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_remove_verifyotp_modified_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VerifyOtp',
        ),
    ]