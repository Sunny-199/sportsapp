# Generated by Django 4.0.3 on 2022-05-05 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0098_rename_sports_center_subscriptionplans_sportcenter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dietplan',
            old_name='evening_snacks',
            new_name='eveningsnacks',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='one_month_plan',
            new_name='onemonthplan',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='one_year_plan',
            new_name='oneyearplan',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='six_months_plans',
            new_name='sixmonthsplans',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='three_months_plan',
            new_name='threemonthsplan',
        ),
    ]
