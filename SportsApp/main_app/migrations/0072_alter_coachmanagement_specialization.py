# Generated by Django 4.0.3 on 2022-04-20 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0071_rename_sportscenterowner_setting_sportcenterowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachmanagement',
            name='specialization',
            field=models.CharField(choices=[('cardio', 'cardio'), ('strength', 'strength')], max_length=100),
        ),
    ]
