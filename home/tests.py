from django.test import TestCase
from .views import index

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/index.html')

    def test_uses_contact_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_uses_about_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'home/about.html')

    def test_uses_works_template(self):
        response = self.client.get('/works/')
        self.assertTemplateUsed(response, 'home/works.html')

