from datetime import date

from django.db import models

# Create your models here.
from django.urls import reverse


class Page(models.Model):
    name = models.CharField('账本名称', max_length=10)
    sum = models.IntegerField('余额', default=0)
    cost = models.IntegerField('花费', default=0)
    lent = models.IntegerField('借出', default=0)
    borrowed = models.IntegerField('余账', default=0)

    class Meta:
        verbose_name = '账本'
        verbose_name_plural = '账本'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page', args=(self.name,))


class Person(models.Model):
    name = models.CharField('用户', max_length=10, db_index=True)
    page = models.ForeignKey(Page, verbose_name='账本', related_name='first')

    def get_absolute_url(self):
        return reverse('person', args=(self.name,))

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name

