# Generated by Django 4.0.3 on 2022-05-16 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0103_auto_20220512_0718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubscriptionPlans',
            new_name='OwnerSubscriptionPlans',
        ),
    ]
