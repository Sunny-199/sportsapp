# Generated by Django 4.0.3 on 2022-04-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0054_remove_usermanagement_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermanagement',
            name='name',
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='last_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
