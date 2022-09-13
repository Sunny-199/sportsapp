# Generated by Django 4.0.3 on 2022-04-07 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='month_plan',
            new_name='one_month_plan',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='months_plan',
            new_name='one_year_plan',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='months_plans',
            new_name='six_months_plans',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='year_plan',
            new_name='three_months_plan',
        ),
    ]
