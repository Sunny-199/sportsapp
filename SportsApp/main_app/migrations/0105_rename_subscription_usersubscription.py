# Generated by Django 4.0.3 on 2022-05-16 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0104_rename_subscriptionplans_ownersubscriptionplans'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscription',
            new_name='UserSubscription',
        ),
    ]
