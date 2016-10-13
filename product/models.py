from __future__ import unicode_literals

from django.db import models

import moneyed
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', verbose_name_plural='Имена')
    slug = models.SlugField(unique=True, verbose_name='URL', verbose_name_plural='URLs')
    description = models.CharField(max_length=255, verbose_name='Описание', verbose_name_plural='Описания')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', verbose_name_plural='Имена')
    slug = models.SlugField(unique=True, verbose_name='URL', verbose_name_plural='URLs')
    description = models.CharField(max_length=255, verbose_name='Описание', verbose_name_plural='Описания')
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='Цена', verbose_name_plural='Цены')
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE, verbose_name='Категория', verbose_name_plural='Категории')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name