# Generated by Django 4.0.3 on 2022-03-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_assignedsportscenter_usermanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplans',
            name='Amount',
            field=models.CharField(max_length=100),
        ),
    ]
