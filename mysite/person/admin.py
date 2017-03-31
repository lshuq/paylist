from django.contrib import admin

# Register your models here.
from .models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'sum', 'cost', 'lent', 'borrowed', ]


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'page', ]


admin.site.register(Page, PageAdmin)
admin.site.register(Person)
