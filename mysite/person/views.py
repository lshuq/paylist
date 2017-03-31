# -*- coding:utf-8 -*-
# !usr/env/bin python3
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from django.template.context_processors import csrf

from person.models import *


@login_required
def person_detail(request, person_name):
    person = Person.objects.get(name=person_name)
    return render(request, 'person/person.html', {'person': person})


@login_required
def page_detail(request, page_name):
    if request.POST:
        tmp = request.POST['tmp']
        fname = request.POST['name']
        if fname != tmp:
            for a in Page.objects.all().values_list('name'):
                if fname in a:
                    return HttpResponse("<p>已存在相同账本，请返回重新输入</p>")
        fsum = request.POST['sum']
        fcost = request.POST['cost']
        flent = request.POST['lent']
        fborrow = request.POST['borrow']
        Page.objects.filter(name=tmp).update(name=fname, sum=fsum, cost=fcost, lent=flent, borrowed=fborrow)
        page_name = fname
    page = Page.objects.get(name=page_name)
    return render(request, 'person/page.html', {'page': page})


@login_required
def index(request):
    persons = Person.objects.all()
    return render(request, 'person/index.html', {'persons': persons})

# 创建新账本/方法未完成
# def page_new(request):
#     if request.POST:
#         fname = request.POST['pagename']
#         for a in Page.objects.all().values_list('name'):
#             if fname in a:
#                 return HttpResponse("<p>已存在相同账本，请返回重新输入</p>")
#         fsum = request.POST['pagesum']
#         fcost = request.POST['pagecost']
#         fborrow = request.POST['pageborrow']
#         new = Page(name=fname, sum=fsum, cost=fcost, borrowed=fborrow)
#         new.save()
