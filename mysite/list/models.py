from django.db import models

# Create your models here.
from django.urls import reverse


class MoneyList(models.Model):
    detail = models.CharField('内容', max_length=200, db_index=True)
    num_in = models.IntegerField('收入', default=0)
    num_out = models.IntegerField('支出', default=0)
    person_in = models.CharField('记账用户', max_length=200)
    person_out = models.CharField('清账用户', max_length=200)
    time = models.DateTimeField('日期', auto_now=True)

    class Meta:
        verbose_name = '账单'
        verbose_name_plural = '账单'

    def get_absolute_url(self):
        return reverse('moneylist', args=(self.detail,))

    def __str__(self):
        return self.detail
