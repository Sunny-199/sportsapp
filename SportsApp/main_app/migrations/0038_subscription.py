# Generated by Django 4.0.3 on 2022-04-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0037_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_plan', models.CharField(max_length=100)),
                ('months_plan', models.CharField(max_length=100)),
                ('months_plans', models.CharField(max_length=100)),
                ('year_plan', models.CharField(max_length=100)),
            ],
        ),
    ]