# Generated by Django 5.1.2 on 2024-11-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='revisions',
            field=models.IntegerField(null=True),
        ),
    ]
