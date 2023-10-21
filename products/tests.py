from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):

    def test_get_home_page_renders(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_product_details_renders(self):
        # reverse function to get the url
        url = reverse('products:product_detail')
        response = self.client.get(url, follow=True) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')
