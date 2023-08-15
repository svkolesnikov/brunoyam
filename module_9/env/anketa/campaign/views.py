from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import DBCampaign, DBAddress, DBCampaign_address, AdvUser
from .forms import CampaignForm, AddressForm


# Create your views here.

def index(response):
    data = DBCampaign.objects.all()
    return render(response, 'private/campaign.html', {'items': data})


def index_adr(response):
    data = DBAddress.objects.all()
    return render(response, 'private/address.html', {'items': data})


@login_required
def campaign_add(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign')
    else:
        # form = CampaignForm()
        form = CampaignForm(initial={'owner_id': request.user.pk})

    context = {'form': form}
    return render(request, 'private/campaign_add.html', context)


@login_required
def campaign_edit(request, pk):
    fm = get_object_or_404(DBCampaign, pk=pk)

    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=fm)
        if form.is_valid():
            form.save()
            return redirect('campaign')
    else:
        form = CampaignForm(instance=fm)

    context = {'form': form}
    return render(request, 'private/campaign_edit.html', context)


@login_required
def campaign_del(request, pk):
    fm = get_object_or_404(DBCampaign, pk=pk)

    if request.method == 'POST':
        fm.delete()
        messages.add_message(request, messages.SUCCESS, 'Кампания удалена')
        return redirect('campaign')
    else:
        context = {'form': fm}
        return render(request, 'private/campaign_del.html', context)


@login_required
def campaign_view(request, pk):
    items = DBCampaign_address.objects.select_related('address_id').filter(campaign_id=pk)

    context = {'pk': pk, 'items': items}
    return render(request, 'private/campaign_view.html', context)

@login_required
def campaign_address_select(request, pk):
    items = DBAddress.objects.exclude(dbcampaign_address__campaign_id=pk)
    context = {'pk': pk, 'items': items}
    return render(request, 'private/campaign_address_select.html', context)


@login_required
def campaign_address_add(request, pk, id):
    flg = DBCampaign_address.objects.filter(campaign_id=pk).filter(address_id=id)

    if len(flg) == 0:
        try:
            rec = DBCampaign_address()
            rec.campaign_id = get_object_or_404(DBCampaign, pk=pk)
            rec.address_id = get_object_or_404(DBAddress, pk=id)
            rec.save()
        except:
            return HttpResponseNotFound("<h2>Неверно заданы параметры запроса</h2>")

    items = DBAddress.objects.exclude(dbcampaign_address__campaign_id=pk)
    context = {'pk': pk, 'items': items}
    return render(request, 'private/campaign_address_select.html', context)

@login_required
def campaign_address_delete(request, pk, id):
    try:
        DBCampaign_address.objects.filter(campaign_id=pk).filter(address_id=id).delete()
        return redirect('campaign_view', pk)
    except:
        return HttpResponseNotFound("<h2>Неверно заданы параметры запроса</h2>")


@login_required
def campaign_user_select(request, pk):
    items = AdvUser.objects.exclude(dbcampaign_user__campaign_id=pk)
    context = {'pk': pk, 'items': items}
    return render(request, 'private/campaign_user_select.html', context)

@login_required
def campaign_user_add(request, pk, id):
    flg = DBCampaign_user.objects.filter(campaign_id=pk).filter(user_id=id)

    if len(flg) == 0:
        try:
            rec = DBCampaign_user()
            rec.campaign_id = get_object_or_404(DBCampaign, pk=pk)
            rec.user_id = get_object_or_404(AdvUser, pk=id)
            rec.save()
        except:
            return HttpResponseNotFound("<h2>Неверно заданы параметры запроса</h2>")

    items = AdvUser.objects.exclude(dbcampaign_user__campaign_id=pk)
    context = {'pk': pk, 'items': items}
    return render(request, 'private/campaign_user_select.html', context)


@login_required
def campaign_user_delete(request, pk, id):
    try:
        DBCampaign_user.objects.filter(campaign_id=pk).filter(user_id=id).delete()
        return redirect('campaign_view', pk)
    except:
        return HttpResponseNotFound("<h2>Неверно заданы параметры запроса</h2>")


@login_required
def address_add(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address')
    else:
        form = AddressForm()

    context = {'form': form}
    return render(request, 'private/address_add.html', context)


@login_required
def address_edit(request, pk):
    fm = get_object_or_404(DBAddress, pk=pk)

    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=fm)
        if form.is_valid():
            form.save()
            return redirect('address')
    else:
        form = CampaignForm(instance=fm)

    context = {'form': form}
    return render(request, 'private/address_edit.html', context)


@login_required
def address_del(request, pk):
    fm = get_object_or_404(DBAddress, pk=pk)

    if request.method == 'POST':
        fm.delete()
        messages.add_message(request, messages.SUCCESS, 'Адрес удален')
        return redirect('address')
    else:
        context = {'form': fm}
        return render(request, 'private/address_del.html', context)
