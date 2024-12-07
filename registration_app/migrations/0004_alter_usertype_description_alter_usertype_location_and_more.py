# Generated by Django 5.1.2 on 2024-10-29 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0003_alter_usertype_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='description',
            field=models.CharField(default='Keine Beschreibung angegeben', max_length=200),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='location',
            field=models.CharField(default='Kein Standort angegeben', max_length=20),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='tel',
            field=models.CharField(default='Keine tel angegeben', max_length=15),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='working_hours',
            field=models.CharField(default='Keine Verfügbarkeit angegeben', max_length=10),
        ),
    ]
