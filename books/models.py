from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"