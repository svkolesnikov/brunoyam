from django.shortcuts import render
from django.http import HttpResponse

from .models import DBCampaign
# Create your views here.

def index(response):
    data = DBCampaign.objects.all()
    return render(response, 'private/campaign.html', {'items':data})

