# Generated by Django 4.0.3 on 2022-04-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0033_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.CharField(max_length=100)),
                ('lunch', models.CharField(max_length=100)),
                ('eveningsnacks', models.CharField(max_length=100)),
                ('dinner', models.CharField(max_length=50)),
            ],
        ),
    ]