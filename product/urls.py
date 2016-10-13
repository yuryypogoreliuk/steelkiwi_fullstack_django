from django.conf.urls import url
from .views import IndexView, CategoryView, ProductView

urlpatterns = [
    url(r'^/$', IndexView.as_view(), name='index'),
    url(r'^(?P<category_slug>[a-zA-Z0-9_\-]*)$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category_slug>[a-zA-Z0-9_\-]*)/(?P<product_slug>[a-zA-Z0-9_\-]*)$', ProductView.as_view(), name='product'),
]