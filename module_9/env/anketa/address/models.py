from django.db import models


# Create your models here.
class DbAddress(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    home = models.CharField(max_length=50, verbose_name='Дом')
    cnt_entrances = models.IntegerField(verbose_name='Количество подъездов')
    cnt_rooms = models.IntegerField(verbose_name='Количество квартир')

    class Meta:
        verbose_name_plural = 'Адрес'
        verbose_name = 'Адрес'
        ordering = ['city']
