import datetime

from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Product, Category


class IndexView(ListView):
    model = Category
    template_name = 'index.html'


class CategoryView(ListView):
    model = Product
    template_name = 'category.html'

    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=slug)

class ProductView(ListView):
    model = Product
    template_name = 'product.html'

    def dispatch(self, request, *args, **kwargs):
        print locals()
        return super(ProductView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        q = get_object_or_404(Product, slug=self.kwargs['product_slug'])
        return q

class LatestProductsView(ListView):

    model = Product
    template_name = 'latest_products.html'

    def dispatch(self, request, *args, **kwargs):
        print locals()
        print 3
        return super(LatestProductsView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        one_day = timezone.now() - datetime.timedelta(days=1)
        return Product.objects.filter(created_at__gte=one_day)
        # print qs
        # return qs

