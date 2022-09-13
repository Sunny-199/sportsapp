# Generated by Django 4.0.3 on 2022-04-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0057_alter_sportscenterowner_timings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachmanagement',
            name='specialization',
            field=models.CharField(choices=[('1', 'cardio'), ('2', 'strength')], default='cardio', max_length=100),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='timings',
            field=models.CharField(blank=True, choices=[('1', '05:00 AM to 06:00 PM')], default=1, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='usermanagement',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20),
        ),
    ]
