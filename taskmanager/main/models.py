from django.db import models
from django.utils.timezone import now
import datetime


class Task(models.Model):
    list_display = ('id', 'title', 'task', 'created')
    fields = ['id', 'title', 'task', 'created']
    id = models.AutoField(primary_key=True)
    title = models.CharField("Наименое задачи", max_length=50)  # Поле с размером до 255 символов. В данном случае не больше 50
    task = models.TextField('Описание')  # Поле с размером более 255 символов
    created = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'