# Generated by Django 5.1.2 on 2024-11-20 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0012_alter_offer_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='user',
            new_name='user_details',
        ),
    ]