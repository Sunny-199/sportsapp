# Generated by Django 4.0.3 on 2022-04-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0083_alter_usermanagement_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='sport',
            field=models.CharField(choices=[('tennis', 'tennis'), ('football', 'football'), ('boxing', 'boxing'), ('wrestling', 'wrestling'), ('cricket', 'cricket')], max_length=60),
        ),
    ]
