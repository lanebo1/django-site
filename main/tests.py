from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class IndexTest(TestCase):
    fixtures = [
        'test_database.json',
    ]

    def test_index_opens(self):
        c = Client()
        resp = c.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)

    def test_auth(self):
        client = Client()
        response = self.client.get(reverse("index"), follow=True)
        url, status_code = response.redirect_chain[-1]
        self.assertIn(reverse("login"), url)


    def test_context(self):
        client = Client()
        response = client.get(reverse("index"))
        self.assertIn(response.context, "current_user")

    def setUp(self):
        self.client = Client()
        user = User.objects.get(username="Test")
        self.client.force_login(user)


class ItemPage(TestCase):
    fixtures = []

    def test_item_page_opens(self):
        c = Client()
        resp = c.get(reverse("tovar"))
        self.assertEqual(resp.status_code, 200)


    def test_item_page_not_found(self):
        c = Client()
        resp = c.get(reverse("tovar"))
        self.assertEqual(resp.status_code, 404)