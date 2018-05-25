from django.db import models


# Create your models here.

class Todo(models.Model):
    project = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    comment = models.TextField()

    # class Meta:
    #     verbose_name='Проект'

    def __str__(self):
        """A string representation of the model."""
        return self.project
