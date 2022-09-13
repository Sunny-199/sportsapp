# Generated by Django 4.0.3 on 2022-03-30 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignedpendingsportscenter',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='assignedpendingsportscenter',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='assignedpendingsportscenter',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='assignedpendingsportscenter',
            old_name='Owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='Sport',
            new_name='sport',
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='SportsCenter',
            new_name='sportscenter',
        ),
        migrations.RenameField(
            model_name='coaches',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='coaches',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='coaches',
            old_name='SportsCenter',
            new_name='sportscenter',
        ),
        migrations.RenameField(
            model_name='coachmanagement',
            old_name='CoachName',
            new_name='coachname',
        ),
        migrations.RenameField(
            model_name='coachmanagement',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='coachmanagement',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='coachmanagement',
            old_name='SportsCenter',
            new_name='sportscenter',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='Coach',
            new_name='coach',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='Package',
            new_name='package',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='SportsCenter',
            new_name='sportscenter',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='Timings',
            new_name='timings',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='UserName',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='sportscenter',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='sportscenter',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='sportscenter',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sportscenter',
            old_name='Timings',
            new_name='timings',
        ),
        migrations.RenameField(
            model_name='sportscenterowner',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='sportscenterowner',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='sportscenterowner',
            old_name='OwnerName',
            new_name='ownername',
        ),
        migrations.RenameField(
            model_name='sportscenterowner',
            old_name='SportsCenter',
            new_name='sportscenter',
        ),
        migrations.RenameField(
            model_name='subscriptionplans',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='subscriptionplans',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='subscriptionplans',
            old_name='Duration',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='subscriptionplans',
            old_name='SportsCenter',
            new_name='sportscenter',
        ),
        migrations.RenameField(
            model_name='transcations',
            old_name='Role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='transcations',
            old_name='SportsCenter',
            new_name='sportscenter',
        ),
        migrations.RenameField(
            model_name='transcations',
            old_name='UserName',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='usermanagement',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='usermanagement',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usermanagement',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='usermanagement',
            old_name='Name',
            new_name='name',
        ),
    ]
