# Generated by Django 4.0.3 on 2022-05-23 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0121_remove_usermanagement_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanagement',
            name='sports_center_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sports_center_owner', to='main_app.sportscenterowner'),
        ),
    ]
