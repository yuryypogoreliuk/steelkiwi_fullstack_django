from django.conf.urls import url, include, patterns
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .views import IndexView, CategoryView, ProductView, LatestProductsView

urlpatterns = [
    url(r'^/$', IndexView.as_view(), name='index'),
    url(r'^(?P<category_slug>[a-zA-Z0-9_\-]*)/$', CategoryView.as_view(), name='category'),
    url(r'^(?P<category_slug>[a-zA-Z0-9_\-]*)/(?P<product_slug>[a-zA-Z0-9_\-]*)/$', ProductView.as_view(), name='product'),
    url(r'^live/$', login_required(LatestProductsView.as_view()), name='latest_24_hours_products')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )