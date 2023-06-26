from django.db import models


# Create your models here.
class BdUser(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    fullname = models.CharField(max_length=50, verbose_name='Фамилия')
    login = models.CharField(max_length=50, verbose_name='Логин')
    password = models.CharField(max_length=50, verbose_name='Пароль')
    email = models.CharField(max_length=50, verbose_name='E-mail')
    phone = models.CharField(max_length=50, verbose_name='Телефон')

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователи'
        ordering = ['-login']


class BdCompany(models.Model):
    name: models.CharField(max_length=50, verbose_name='Название кампании')
    user_id = models.ForeignKey('BdUser', null='True', on_delete=models.PROTECT, verbose_name='Пользователь')

    class Meta:
        verbose_name_plural = 'Кампания'
        verbose_name = 'Кампания'
        #ordering = ['name']


class BdHome(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    home = models.CharField(max_length=50, verbose_name='Дом')
    cnt_entrances = models.IntegerField(verbose_name='Количество подъездов')
    cnt_rooms = models.IntegerField(verbose_name='Количество квартир')

    class Meta:
        verbose_name_plural = 'Адрес'
        verbose_name = 'Адрес'
        ordering = ['city']

#class BdCompany(models.Model):
#    name: models.CharField(max_length=50)
