# Generated by Django 4.2.1 on 2023-06-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_order_date_added_alter_order_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Totalprice',
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]
