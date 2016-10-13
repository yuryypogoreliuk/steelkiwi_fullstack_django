from django.shortcuts import render
from django.views.generic import View

from .models import Product, Category

class IndexView(View):
    model = Category

    def get(self):
        pass

class CategoryView(View):
    model = Category

    def get(self):
        pass

class ProductView(View):
    model = Product

    def get(self):
        pass
