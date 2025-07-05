from django.db import models


statuses = [("active", "Активно"), ("blocked", "Заблокировано")]

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Имя")
    email = models.EmailField(null=False, blank=False, verbose_name="Почта")
    text = models.TextField(null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    statuses = models.CharField(max_length=20, choices=statuses, default="active", verbose_name="Статус")

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = 'books'
        verbose_name = 'Сообщение'
        verbose_name_plural = "Сообщения"