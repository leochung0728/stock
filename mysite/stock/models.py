# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Stock(models.Model):
    code = models.CharField(max_length=20, verbose_name='股票代號', unique=True)
    name = models.CharField(max_length=50, verbose_name='股票名稱')

    def __unicode__(self):
        return self.name

class Transaction(models.Model):
    code = models.ForeignKey(Stock, verbose_name='股票代號')
    date = models.DateField(verbose_name='交易日期')
    volume = models.DecimalField(max_digits=10, decimal_places=0, null=True, verbose_name='成交量')
    final_price = models.DecimalField(max_digits=13, decimal_places=0, null=True, verbose_name='成交金額')
    opening_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='開盤價')
    closing_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='收盤價')
    highest_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='最高價')
    lowest_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='最低價')
    price_diff = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='漲跌')

    def __unicode__(self):
        return '{}({})'.format(self.code, self.date)

    class Meta:
        unique_together = ('code', 'date')