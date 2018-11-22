from django.db import models

class Good(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    status = models.ForeignKey('Status', on_delete=None, verbose_name='Статус')
    qty = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'Статусы товара'
