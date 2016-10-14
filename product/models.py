# coding: utf-8
from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone

import moneyed
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.CharField(max_length=255, verbose_name='Описание')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='Цена')
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE, verbose_name='Категория')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def was_created_recently(self):
        one_day = timezone.now() - datetime.timedelta(days=1)
        return self.pub_date >= one_day

    class Meta:
        get_latest_by = 'created_at'
        order_with_respect_to = 'category'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __unicode__(self):
        return self.name

