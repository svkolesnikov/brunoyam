from django.db import models
from django.utils.timezone import now

from main.models import AdvUser




# Create your models here.
class DBCampaign(models.Model):
    name = models.CharField(max_length=50, null=False, default='', verbose_name='Название кампании')
    owner_id = models.ForeignKey(AdvUser, null=True, on_delete=models.PROTECT, verbose_name='ID Пользователя')

    class Meta:
        verbose_name_plural = 'Кампании'
        verbose_name = 'Кампания'


class DBAddress(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    home = models.CharField(max_length=50, verbose_name='Дом')
    cnt_entrances = models.IntegerField(verbose_name='Количество подъездов')
    cnt_rooms = models.IntegerField(verbose_name='Количество квартир')

    class Meta:
        verbose_name_plural = 'Адрес'
        verbose_name = 'Адрес'
        ordering = ['city']


class DBCampaign_address(models.Model):
    campaign_id: models.ForeignKey(DBCampaign, null=True, on_delete=models.PROTECT, verbose_name='ID Кампании')
    address_id: models.ForeignKey(DBAddress, null=True, on_delete=models.PROTECT, verbose_name='ID дома')

    class Meta:
        verbose_name_plural = 'Связь Кампании с адресом дома'
        verbose_name = 'Связь'


class DBCampaign_user(models.Model):
    campaign_id= models.ForeignKey(DBCampaign, null=True, on_delete=models.PROTECT, verbose_name='ID Кампании')
    user_id= models.ForeignKey(AdvUser, null=True, on_delete=models.PROTECT, verbose_name='ID Пользователя')

    class Meta:
        verbose_name_plural = 'Связь Кампании с пользователем'
        verbose_name = 'Связь'


class DBState(models.Model):
    name= models.CharField(max_length=20, null=True, verbose_name='Реакция жильцов')

    class Meta:
        verbose_name_plural = 'Реакции жильцов'
        verbose_name = 'Реакция'


class DBAnketa(models.Model):
    campaign_id= models.ForeignKey(DBCampaign, null=True, on_delete=models.PROTECT, verbose_name='ID Кампании')
    address_id= models.ForeignKey(DBAddress, null=True, on_delete=models.PROTECT, verbose_name='ID дома')
    user_id= models.ForeignKey(AdvUser, null=True, on_delete=models.PROTECT, verbose_name='ID Пользователя')
    published= models.DateTimeField(default=now, db_index=True, blank=True, verbose_name='Дата опроса')
    room= models.CharField(max_length=20, null=True, verbose_name='Квартира')
    open_door= models.BooleanField(null=False, default=False, verbose_name='Открыли дверь')
    name= models.CharField(max_length=200, null=True, verbose_name='ФИО')
    phone= models.CharField(max_length=20, null=True, verbose_name='Телефон')
    state= models.ForeignKey(DBState, on_delete=models.PROTECT, null=True, verbose_name='Реакция жильцов')
    note= models.TextField(verbose_name='Заметки', null=True)

    class Meta:
        verbose_name_plural = 'Анкеты'
        verbose_name = 'Анкета'
