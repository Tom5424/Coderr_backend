# Generated by Django 5.1.2 on 2024-11-29 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0015_offer_user_alter_offer_user_details'),
        ('reviews_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='business_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_user', to='offers_app.offer'),
        ),
    ]