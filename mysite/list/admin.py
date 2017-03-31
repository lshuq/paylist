from django.contrib import admin

# Register your models here.
from list.models import *


class MoneyListAdmin(admin.ModelAdmin):
    list_display = ['detail', 'num_in', 'num_out', 'person_in', 'person_out', 'time']
    search_fields = ['time']


admin.site.register(MoneyList, MoneyListAdmin)
