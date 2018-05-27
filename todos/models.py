from django.db import models


# Create your models here.

#
# class Team(models.Model):
#     name = models.CharField(max_length=30, verbose_name="Команда")
#     description = models.TextField(verbose_name="Описание")
#
#     def __str__(self):
#         return self.name


class Deploy(models.Model):
    project = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.project

