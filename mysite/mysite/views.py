from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.context_processors import csrf


def home_site(request):
    return render(request, 'home_site.html')
