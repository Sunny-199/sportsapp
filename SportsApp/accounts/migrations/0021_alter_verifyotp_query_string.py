# Generated by Django 4.0.3 on 2022-04-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_verifyotp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifyotp',
            name='query_string',
            field=models.CharField(max_length=50),
        ),
    ]
