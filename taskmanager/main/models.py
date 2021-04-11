from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)  # Поле с размером до 255 символов. В данном случае не больше 50
    task = models.TextField('Описание')  # Поле с размером более 255 символов

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'