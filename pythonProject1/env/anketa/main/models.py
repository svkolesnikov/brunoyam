from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    phone = models.CharField(max_length=30, verbose_name='Телефон')

    class Meta(AbstractUser.Meta):
        pass
