from django import forms

from .models import DBCampaign, DBAddress, DBAnketa

class CampaignForm(forms.ModelForm):
    class Meta:
        model = DBCampaign
        fields = '__all__'
        widgets = {'owner_id': forms.HiddenInput}


class AddressForm(forms.ModelForm):
    class Meta:
        model = DBAddress
        fields = '__all__'

class SurveyForm(forms.ModelForm):
    class Meta:
        model = DBAnketa
        fields= '__all__'
        #widgets = {'user_id': forms.HiddenInput, 'campaign_id':forms.HiddenInput, 'address_id':forms.HiddenInput}

