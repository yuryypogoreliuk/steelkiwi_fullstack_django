from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Product, Category

class IndexView(ListView):
    model = Category
    template_name = 'index.html'

    def get_queryset(self):
        qs = Category.objects.all()
        return qs

    def get(self):
        pass

class CategoryView(ListView):
    model = Category
    template_name = 'category.html'

    def get_queryset(self):
        qs = Product.objects.filter(category__slug=self.request['category_slug'])
        category = get_object_or_404(Category, slug=self.request['category_slug'])


    def get(self):
        pass

class ProductView(ListView):
    model = Product
    template_name = 'product.html'

    def get_queryset(self):
        product = get_object_or_404(Product, slug=self.request['product_slug'])

    def get(self):
        pass

class LatestProductsView(ListView):
    
    template_name = 'latest_products.html'

    def get_queryset(self):
        products = Product.get_latest_products()

    def get(self):
        pass
