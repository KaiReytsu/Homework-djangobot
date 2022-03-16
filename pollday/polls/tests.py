from http import HTTPStatus
from django.test import TestCase
from django.http import HttpRequest
from .views import index

class PollTestCase(TestCase):

    def test_index(self):
        self.assertEqual(
            index(HttpRequest()).status_code,
            HTTPStatus.OK
        )