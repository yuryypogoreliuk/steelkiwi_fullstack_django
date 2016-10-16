from django.conf.urls import url, include, patterns
#from django.contrib.auth.decorators import login_required
from django.conf import settings

from .views import IndexView, CategoryView, ProductView, LatestProductsView

urlpatterns = [
    # /products/
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),

    # /products/live/
    url(
        r'^live/$',
        LatestProductsView.as_view(),
        name='latest_products'
    ),
    # /products/<category_slug>/
    url(
        r'^(?P<category_slug>[a-zA-Z0-9_\-]*)/$',
        CategoryView.as_view(),
        name='category'
    ),
    # /products/<category_slug>/<product_slug>
    url(
        r'^(?P<category_slug>[a-zA-Z0-9_\-]*)/(?P<product_slug>[a-zA-Z0-9_\-]*)/$',
        ProductView.as_view(),
        name='product'
    ),
    #

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )