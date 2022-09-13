# Generated by Django 4.0.3 on 2022-05-19 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0118_alter_coaches_sportscenter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermanagement',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usermanagement',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='usermanagement',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='usermanagement',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='usermanagement',
            name='location',
        ),
        migrations.RemoveField(
            model_name='usermanagement',
            name='phoneno',
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='sports_center_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sports_center_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermanagement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='normal_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
