# Generated by Django 4.0.3 on 2022-03-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_alter_schedule_timings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='Timings',
            field=models.CharField(blank=True, choices=[('05:00 AM', '05:00 AM to 06:00 PM')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='sportscenter',
            name='Timings',
            field=models.CharField(blank=True, choices=[('05:00 AM', '05:00 AM-08:00 PM')], max_length=30, null=True),
        ),
    ]
