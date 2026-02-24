from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test123")

    def test_aktivnosti_view(self):
        self.client.login(username="test", password="test123")
        response = self.client.get(reverse("volonteri:aktivnost_list"))
        self.assertEqual(response.status_code, 200)
