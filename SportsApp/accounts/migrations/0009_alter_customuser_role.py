# Generated by Django 4.0.3 on 2022-04-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('coaches', 'Coaches'), ('owner', 'Owner')], max_length=20),
        ),
    ]
