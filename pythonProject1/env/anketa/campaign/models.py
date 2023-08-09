from django.db import models

from main.models import AdvUser


# Create your models here.
class DBCampaign(models.Model):
    name: models.CharField(max_length=50, verbose_name='Название кампании')
    owner_id: models.ForeignKey(AdvUser, null=True, on_delete=models.PROTECT, verbose_name='ID Пользователя')

    class Meta:
        verbose_name_plural = 'Кампании'
        verbose_name = 'Кампания'


class DBHome(models.Model):
    city: models.CharField(max_length=50, verbose_name='Город', db_index=True)
    street: models.CharField(max_length=250, verbose_name='Улица', db_index=True)
    home: models.CharField(max_length=50, verbose_name='Дом', db_index=True)
    cnt_entrance: models.IntegerField(verbose_name='Количество подъездов')
    cnt_rooms: models.IntegerField(verbose_name='Количество квартир')

    class Meta:
        verbose_name_plural = 'Дома'
        verbose_name = 'Дом'


class DBCampaign_home(models.Model):
    campaign_id: models.ForeignKey(DBCampaign, null=True, on_delete=models.PROTECT, verbose_name='ID Кампании')
    home_id: models.ForeignKey(DBHome, null=True, on_delete=models.PROTECT, verbose_name='ID дома')

    class Meta:
        verbose_name_plural = 'Связь Кампании с домом'
        verbose_name = 'Связь'


class DBCampaign_user(models.Model):
    campaign_id: models.ForeignKey(DBCampaign, null=True, on_delete=models.PROTECT, verbose_name='ID Кампании')
    user_id: models.ForeignKey(AdvUser, null=True, on_delete=models.PROTECT, verbose_name='ID Пользователя')

    class Meta:
        verbose_name_plural = 'Связь Кампании с пользователем'
        verbose_name = 'Связь'


class DBState(models.Model):
    name: models.CharField(max_length=20, null=True, verbose_name='Реакция жильцов')

    class Meta:
        verbose_name_plural = 'Реакции жильцов'
        verbose_name = 'Реакция'


class DBAnketa(models.Model):
    campaign_id: models.ForeignKey(DBCampaign, null=True, on_delete=models.PROTECT, verbose_name='ID Кампании')
    home_id: models.ForeignKey(DBHome, null=True, on_delete=models.PROTECT, verbose_name='ID дома')
    user_id: models.ForeignKey(AdvUser, null=True, on_delete=models.PROTECT, verbose_name='ID Пользователя')
    published: models.DateTimeField(auto_now_add=True, verbose_name='Дата опроса')
    room: models.CharField(max_length=20, verbose_name='Квартира')
    open_door: models.BooleanField(null=False, default=False, verbose_name='Открыли дверь')
    name: models.CharField(max_length=200, null=True, verbose_name='ФИО')
    phone: models.CharField(max_length=20, null=True, verbose_name='Телефон')
    state: models.ForeignKey(DBState, on_delete=models.PROTECT, null=True, verbose_name='Реакция жильцов')
    note: models.TextField(verbose_name='Заметки')

    class Meta:
        verbose_name_plural = 'Анкеты'
        verbose_name = 'Анкета'
