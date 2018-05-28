from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#
# class Team(models.Model):
#     name = models.CharField(max_length=30, verbose_name="Команда")
#     description = models.TextField(verbose_name="Описание")
#
#     def __str__(self):
#         return self.name


class Deploy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    project = models.CharField(max_length=200)
    version = models.FloatField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project


# Простые поля:
#Класс поля           - Тип данных
#models.IntegerField  - целое число
#models.DateTimeField - дата и время
#models.BooleanField  - логический
#models.CharField     - строковый
#models.FloatField    - вещественный
#models.TextField     - текст
#models.TimeField     - время
#models.AutoField     - счетчик

# Производные поля
#Класс поля                       - Тип данных
#models.EmailField                - email
#models.IPAddressField            - ipv4
#models.GenericIPAddressField     - ipv4 or ipv6
#models.URLField                  - url