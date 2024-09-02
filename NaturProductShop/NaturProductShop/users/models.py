from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    userId = models.AutoField(primary_key=True, verbose_name='Номер пользователя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Employee(models.Model):
    EMPLOYEE_JOB_TITLE_CHOICES = [
        ("АД", "Администратор"),
        ("МД", "Менеджер доставок"),
    ]
    user = models.OneToOneField(User, models.CASCADE, verbose_name='Пользователь')
    employeeJobTitle = models.TextField(choices=EMPLOYEE_JOB_TITLE_CHOICES, verbose_name='Должность')

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'

class Request(models.Model):
    title = models.TextField(default='Обращение в поддержку', max_length=50, verbose_name='Нименование запроса')
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='Пользователь')
    userEmail = models.EmailField(max_length=30, verbose_name='Электронная почта пользователя')
    requestText = models.TextField(verbose_name='Текст запроса')
    answerText = models.TextField(default='Ждите ответ менеджера', verbose_name='Текст ответа')

    class Meta:
        verbose_name = 'Запросы пользователей'
        verbose_name_plural = 'Запросы пользователей'



