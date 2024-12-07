# Generated by Django 5.1.2 on 2024-11-26 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0015_offer_user_alter_offer_user_details'),
        ('orders_app', '0004_alter_order_price'),
        ('registration_app', '0009_alter_customprofile_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='business_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_user', to='registration_app.customprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_user', to='registration_app.customprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='offer_detail_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='offers_app.offerdetail'),
        ),
    ]
