# Generated by Django 5.0.6 on 2024-05-30 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_productstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderPhoneNumber',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Неверный формат телефона', regex='^\\+?7?\\d{9,11}$')]),
        ),
    ]
