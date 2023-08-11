from django.shortcuts import render
from ..campaign.models import DBAddress
# Create your views here.
def index(response):
    data = DBAddress.objects.all()
    return render(response, 'private/campaign.html', {'items':data})