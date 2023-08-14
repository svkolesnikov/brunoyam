from django import forms

from .models import DBCampaign, DBAddress

class CampaignForm(forms.ModelForm):
    class Meta:
        model = DBCampaign
        fields = '__all__'
        widgets = {'owner_id': forms.HiddenInput}


class AddressForm(forms.ModelForm):
    class Meta:
        model = DBAddress
        fields = '__all__'




