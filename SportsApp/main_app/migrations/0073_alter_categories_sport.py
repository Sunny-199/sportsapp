# Generated by Django 4.0.3 on 2022-04-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0072_alter_coachmanagement_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='sport',
            field=models.CharField(choices=[('tennis', 'tennis'), ('football', 'football'), ('boxing', 'boxing'), ('wrestling', 'wrestling')], max_length=60),
        ),
    ]
