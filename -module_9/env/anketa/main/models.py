from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    birthday = models.DateField(null=True, verbose_name='Дата рождения')
    address = models.TextField(null=True, verbose_name='Адрес')
    sex = models.CharField(null=True, max_length=1, verbose_name='Пол')

    class Meta(AbstractUser.Meta):
        pass


