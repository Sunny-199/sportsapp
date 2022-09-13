# Generated by Django 4.0.3 on 2022-04-04 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0035_alter_schedule_timings_alter_sportscenter_timings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssignedPendingSportsCenter',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Coaches',
        ),
        migrations.DeleteModel(
            name='CoachManagement',
        ),
        migrations.DeleteModel(
            name='DietPlan',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='SportsCenter',
        ),
        migrations.DeleteModel(
            name='SportsCenterOwner',
        ),
        migrations.DeleteModel(
            name='SubscriptionPlans',
        ),
        migrations.DeleteModel(
            name='TranscationDetail',
        ),
        migrations.DeleteModel(
            name='Transcations',
        ),
        migrations.DeleteModel(
            name='UserManagement',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]