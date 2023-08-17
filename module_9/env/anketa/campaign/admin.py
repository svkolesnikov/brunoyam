from django.contrib import admin
from .models import DBCampaign, DBCampaign_user, DBAddress, DBCampaign_address, DBState, DBAnketa

# Register your models here.
admin.site.register(DBCampaign)
admin.site.register(DBCampaign_user)
admin.site.register(DBAddress)
admin.site.register(DBCampaign_address)
admin.site.register(DBAnketa)
admin.site.register(DBState)


