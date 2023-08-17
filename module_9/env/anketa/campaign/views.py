from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Count, Sum, Q, Subquery

from .models import DBCampaign, DBAddress, DBCampaign_address, DBCampaign_user, AdvUser, DBAnketa
from .forms import CampaignForm, AddressForm, SurveyForm


# Create your views here.

@login_required
def index(request):
    cmp = DBCampaign_user.objects.filter(user_id=request.user.pk)
    data = DBCampaign.objects.filter(Q(owner_id=request.user.pk) | Q(id__in= Subquery(cmp.values('campaign_id')))  )

    return render(request, 'private/campaign.html', {'items': data})

@login_required
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
    items_cmp = DBCampaign_address.objects.select_related('address_id').filter(campaign_id=pk)
    items_user = DBCampaign_user.objects.select_related('user_id').filter(campaign_id=pk)

    context = {'pk': pk, 'items_cmp': items_cmp, 'items_user': items_user}

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


@login_required
def survey_add(request, pk, id):
    if request.method == 'POST':
        print(1)
        form = SurveyForm(request.POST)
        # form['campaign_id'] = pk
        # form['address_id'] = id
        print(request.POST)
        if form.is_valid():
            print(2)
            form.save()
            return redirect('campaign_view', pk=pk)
    else:
        print(3)
        form = SurveyForm(initial={'user_id': request.user.pk, 'campaign_id': pk, 'address_id': id})

    context = {'form': form}
    return render(request, 'private/survey_add.html', context)


@login_required
def address_state(request, pk, id):
    items = DBAnketa.objects.filter(campaign_id=id).filter(address_id=id)
    context = {'items': items, 'pk': pk}
    return render(request, 'private/address_state.html', context)


@login_required
def campaign_stat(request, pk):
    # Сколько всего дверей
    doors = DBAddress.objects.filter(dbcampaign_address__campaign_id=pk).aggregate(Sum('cnt_rooms'))
    doors_open = DBAnketa.objects.filter(campaign_id=pk).filter(open_door=True).aggregate(Count('open_door'))
    doors_close = DBAnketa.objects.filter(campaign_id=pk).filter(open_door=False).aggregate(Count('open_door'))

    pc_doors_open = 0
    pc_doors_close = 0
    if doors['cnt_rooms__sum'] > 0:
        pc_doors_open = doors_open['open_door__count'] / doors['cnt_rooms__sum'] * 100
        pc_doors_close = doors_close['open_door__count'] / doors['cnt_rooms__sum'] * 100

    # items = DBAnketa.objects.filter(campaign_id=pk).annotate(dc=Count('open_door', open_door=False),
    #                                                         do=Count('open_door', open_door=True))

    items = DBAnketa.objects.filter(campaign_id=pk).values('address_id__city', 'address_id__street',
                                                           'address_id__home').annotate(
        do=Count('open_door', filter=Q(open_door=True)), dc=Count('open_door', filter=Q(open_door=False)))


    items_state = DBAnketa.objects.filter(campaign_id=pk) \
                                  .values('address_id__city', 'address_id__street', 'address_id__home') \
                                  .annotate(positive=Count('state', filter=Q(state=1)), \
                                            negative=Count('state', filter=Q(state=2)))

    cnt_contact = DBAnketa.objects.filter(campaign_id=pk).exclude(name='').aggregate(cnt = Count('name'))
    print(cnt_contact)

    context = {'items': items, 'pk': pk,
               'doors': doors['cnt_rooms__sum'],
               'pc_doors_open': pc_doors_open,
               'pc_doors_close': pc_doors_close,
               'items_state': items_state,
               'cnt_contact':cnt_contact['cnt']}
    return render(request, 'private/campaign_stat.html', context)
