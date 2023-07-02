from django.db import models

# Create your models here.


class task(models.Model):
    title = models.TextField('url')
    task = models.TextField('result')

    def __str__(self):
        return self.task
    class Meta:
        verbose_name='Запрос'
        verbose_name_plural="Запросы"