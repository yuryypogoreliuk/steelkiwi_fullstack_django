import datetime

from django.utils import timezone
from django.test import TestCase
from django.test import Client

from .models import Category

client = Client()

class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_latest_products(self):

        response = self.client.get('/products/')
        self.assert_(response.status_code in [200, 301, 302])
        categories_count = Category.objects.count()
        print response.context
        #print response.context['object_list']
        #self.assertEqual(response.context[''])

        