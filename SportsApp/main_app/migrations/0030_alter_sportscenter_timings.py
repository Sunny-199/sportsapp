# Generated by Django 4.0.3 on 2022-03-31 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0029_rename_phone number_assignedpendingsportscenter_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportscenter',
            name='timings',
            field=models.CharField(blank=True, choices=[('05:00 AM-08:00 PM', '05:00 AM-08:00 PM'), ('06:00 AM-09:00 PM', '06:00 AM-08:00 PM')], max_length=30, null=True),
        ),
    ]