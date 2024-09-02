# Generated by Django 4.2.7 on 2023-12-14 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_request'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудники', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Запросы пользователей', 'verbose_name_plural': 'Запросы пользователей'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователи', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='request',
            name='answerText',
            field=models.TextField(default='Ждите ответ менеджера', verbose_name='Текст ответа'),
        ),
        migrations.AddField(
            model_name='request',
            name='title',
            field=models.TextField(default='Обращение в поддержку', max_length=50, verbose_name='Нименование запроса'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeJobTitle',
            field=models.TextField(choices=[('АД', 'Администратор'), ('МД', 'Менеджер доставок')], verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='request',
            name='requestText',
            field=models.TextField(verbose_name='Текст запроса'),
        ),
        migrations.AlterField(
            model_name='request',
            name='userEmail',
            field=models.EmailField(max_length=30, verbose_name='Электронная почта пользователя'),
        ),
        migrations.AlterField(
            model_name='request',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Номер пользователя'),
        ),
    ]