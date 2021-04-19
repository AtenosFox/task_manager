from django.db import models


class Task(models.Model):
    list_display = ('id', 'title', 'task')
    fields = ['id', 'title', 'task']
    id = models.AutoField(primary_key=True)
    title = models.CharField("Наименое задачи", max_length=50)  # Поле с размером до 255 символов. В данном случае не больше 50
    task = models.TextField('Описание')  # Поле с размером более 255 символов

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'