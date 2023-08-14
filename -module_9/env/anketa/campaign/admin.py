from django.contrib import admin
from .models import DBCampaign, DBCampaign_user

# Register your models here.
admin.site.register(DBCampaign)
admin.site.register(DBCampaign_user)

