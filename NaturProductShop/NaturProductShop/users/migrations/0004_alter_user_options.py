# Generated by Django 5.0.6 on 2024-06-18 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_employee_options_alter_request_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
