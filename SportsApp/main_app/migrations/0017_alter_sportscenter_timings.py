# Generated by Django 4.0.3 on 2022-03-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_subscriptionplans_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportscenter',
            name='Timings',
            field=models.CharField(blank=True, choices=[('02 AM', '05 AM'), ('05 AM', '08 AM'), ('08 AM', '11 AM'), ('11 AM', '02 PM'), ('02 PM', '05 PM'), ('05 PM', '08 PM'), ('08 PM', '11 PM'), ('11 PM', '01 AM')], default=None, max_length=30),
            preserve_default=False,
        ),
    ]