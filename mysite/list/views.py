from datetime import datetime

from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import csrf

from list.models import *


@login_required
def money_list(request):
    if request.POST:
        form = ListForm(request.POST)
        if form.is_valid():
            new_detail = form.cleaned_data['detail']
            for a in MoneyList.objects.all().values_list('detail'):
                if new_detail in a:
                    return HttpResponse("<p>已存在相同账单，请返回重新输入</p>")
            new_num_in = form.cleaned_data['num_in']
            new_num_out = form.cleaned_data['num_out']
            new_person_in = form.cleaned_data['person_in']
            new_person_out = form.cleaned_data['person_in']
            # new_time = request.POST['time']
            new_record = MoneyList(detail=new_detail, num_in=new_num_in, num_out=new_num_out, person_in=new_person_in,
                                   person_out=new_person_out,
                                   )
            new_record.save()
    form = ListForm()
    ctx = {}
    ctx.update(csrf(request))
    all_records = MoneyList.objects.all()
    ctx['moneyList'] = all_records
    ctx['form'] = form
    return render(request, 'mysite/moneyList.html', ctx)


class ListForm(forms.Form):
    detail = forms.CharField(max_length=200, label='账单内容')
    num_in = forms.IntegerField(label='收入    ')
    num_out = forms.IntegerField(label='支出    ')
    person_in = forms.CharField(max_length=200, label='记账人  ')


@login_required
def list_detail(request, mylist):
    moneylist = MoneyList.objects.get(detail=mylist)
    if request.POST:
        n_num_in = request.POST['num_in']
        n_num_out = request.POST['num_out']
        n_p_out = request.POST['checker']
        n_id = request.POST['id']
        n_num_in = int(n_num_in) - int(n_num_out)
        MoneyList.objects.filter(id=n_id).update(num_in=n_num_in, num_out=0, person_out=n_p_out)
        moneylist = MoneyList.objects.get(detail=mylist)
    return render(request, 'mysite/listdetail.html', {'moneylist': moneylist})


@login_required
def searched_list(request):
    moneylist = {}
    if request.POST:
        year = request.POST['year_from']
        month = request.POST['month_from']
        day = request.POST['day_from']
        date_from = datetime(int(year), int(month), int(day), 0, 0, 0)
        year = request.POST['year_to']
        month = request.POST['month_to']
        day = request.POST['day_to']
        date_to = datetime(int(year), int(month), int(day), 23, 59, 59)
        moneylist = MoneyList.objects.filter(time__range=(date_from, date_to))
    return render(request, 'mysite/searched.html', {'moneylist': moneylist})


@login_required
def search_list(request):
    return render(request, 'mysite/search.html')


@login_required
def list_day(request):
    now = datetime.now()
    day = (datetime(now.year, now.month, 1) - datetime(now.year, now.month - 1, 1)).days
    if now.day == 1:
        first = datetime(now.year, now.month - 1, day, now.hour, now.minute, now.second)
    else:
        first = datetime(now.year, now.month, now.day - 1, now.hour, now.minute, now.second)
    end = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    moneylist = MoneyList.objects.filter(time__range=(first, end))
    return render(request, 'mysite/day.html', {'moneylist': moneylist})


@login_required
def list_week(request):
    now = datetime.now()
    day = (datetime(now.year, now.month, 1) - datetime(now.year, now.month - 1, 1)).days
    if now.day < 8:
        first = datetime(now.year, now.month - 1, now.day + day - 7, now.hour, now.minute, now.second)
    else:
        first = datetime(now.year, now.month, now.day - 7, now.hour, now.minute, now.second)
    end = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    moneylist = MoneyList.objects.filter(time__range=(first, end))
    return render(request, 'mysite/week.html', {'moneylist': moneylist})


@login_required
def list_month(request):
    now = datetime.now()
    day = (datetime(now.year, now.month, 1) - datetime(now.year, now.month - 1, 1)).days
    if now.day > day:
        first = datetime(now.year, now.month - 1, day, now.hour, now.minute, now.second)
    else:
        first = datetime(now.year, now.month - 1, now.day, now.hour, now.minute, now.second)
    end = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    moneylist = MoneyList.objects.filter(time__range=(first, end))
    return render(request, 'mysite/month.html', {'moneylist': moneylist})
