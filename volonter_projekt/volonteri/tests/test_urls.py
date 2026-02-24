from django.test import SimpleTestCase
from django.urls import reverse, resolve
from volonteri.views import *

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('volonteri:index')
        self.assertEqual(resolve(url).func, index)

    def test_aktivnosti_list_url(self):
        url = reverse('volonteri:aktivnost_list')
        self.assertEqual(resolve(url).func.view_class, ActivityListView)

    def test_aktivnost_detail_url(self):
        url = reverse('volonteri:aktivnost_detalji', args=[1])
        self.assertEqual(resolve(url).func.view_class, AktivnostDetailView)

    def test_aktivnost_create_url(self):
        url = reverse('volonteri:aktivnost_nova')
        self.assertEqual(resolve(url).func.view_class, AktivnostCreateView)

    def test_aktivnost_update_url(self):
        url = reverse('volonteri:aktivnost_uredi', args=[1])
        self.assertEqual(resolve(url).func.view_class, AktivnostUpdateView)

    def test_aktivnost_delete_url(self):
        url = reverse('volonteri:aktivnost_obrisi', args=[1])
        self.assertEqual(resolve(url).func.view_class, AktivnostDeleteView)
