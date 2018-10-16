# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class StripePayment(models.Model):
    """
    It's store the payment related information excluding card information.
    """
    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('AED', 'AED'),
        ('SGD', 'SGD')
    )

    name = models.CharField(max_length=52, verbose_name='Name', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    amount = models.CharField(max_length=12)
    transaction_id = models.CharField(max_length=126, null=True, blank=True)
    currency = models.CharField(max_length=15, choices=CURRENCY_CHOICES, default='USD')


    def __unicode__(self):
        return '{0}'.format(self.name)
