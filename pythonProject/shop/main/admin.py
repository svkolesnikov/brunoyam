from django.contrib import admin
from .models import BdUser, BdHome, BdCompany

admin.site.register(BdUser)
admin.site.register(BdHome)
admin.site.register(BdCompany)
