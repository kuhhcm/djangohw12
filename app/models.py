from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=20, verbose_name='Статус')
    deadline = models.DateField(verbose_name='Дедлайн')
    
    def __str__(self) -> str:
        return f"{self.title} - {self.deadline}"
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
