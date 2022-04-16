from django.test import TestCase, Client
from django.urls import reverse


class IndexTest(TestCase):
    fixtures = []

    def test_index_opens(self):
        c = Client()
        resp = c.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)


