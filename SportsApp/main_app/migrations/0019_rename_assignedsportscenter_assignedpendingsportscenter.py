# Generated by Django 4.0.3 on 2022-03-29 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_alter_sportscenter_timings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssignedSportsCenter',
            new_name='AssignedPendingSportsCenter',
        ),
    ]
