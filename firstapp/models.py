from django.db import models


# Create your models here.

class ArtifactBox(models.Model):
    name = models.CharField(max_length=30, verbose_name='Артефакты')
    description = models.TextField(default=0, verbose_name='Описание')
    version = models.FloatField(verbose_name='Версия')
    url = models.URLField(verbose_name='Веб-адрес проекта')

    def __str__(self):
        return  self.name

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
