# Generated by Django 4.2.7 on 2023-12-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_ordercost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderCost',
            field=models.IntegerField(),
        ),
    ]
