# Generated by Django 3.2.8 on 2023-08-12 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_address_assignment_customer_deliverystatus_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='AddressID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.address'),
        ),
    ]
