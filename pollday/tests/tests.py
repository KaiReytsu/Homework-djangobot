from http import HTTPStatus
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from datetime import datetime

class PollTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_dtnow(self):
        url = reverse('dtnow')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'polls/dtnow.html')

    def test_dt(self):
        url = reverse('dtnow')
        response = self.client.get(url)
        self.assertContains(response, datetime.now().strftime('%d-%m-%Y %a %H:%M'))

#Запуск тестов python3 manage.py test 
# (либо указывать папку с тестами, либо директорую, 
# в которой находится файл с тестом, либо название файла, если не test)