# Generated by Django 5.1.2 on 2024-11-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0002_alter_order_revisions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time_in_days',
            field=models.PositiveIntegerField(null=True),
        ),
    ]