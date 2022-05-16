from turtle import title
from urllib import response
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from . import models

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup(self):
        '''Тест для проверки страницы регистрации.'''
        response = self.client.post('/polls/signup/', {'username': 'qwe',
        'first_name': 'qwe','password1': 'kuuJei0v', 'password2': 'kuuJei0v',
        'email': 'test@test.com'})
        #Если данные при регситрации введены правильно, про происходит редирект на страницу логина
        self.assertEqual(response.status_code, 302) #Проверка стутас кода
        self.assertEqual(response.url, '/polls/login/') #Проверка корректного редиректа

    def test_login_success(self):
        '''Тест для проверки успешного входа.'''
        user = User.objects.create(username='test')
        user.set_password('kuuJei0v')
        user.save()
        login = self.client.login(username = 'test', password = 'kuuJei0v')
        response = self.client.post('/polls/login/', {'username': 'test', 'password': 'kuuJei0v'})
        self.assertTrue(login) #Проверка успешного входв в систему
        #При успешном входе происходит редирект на страницу welcompage
        self.assertEqual(response.status_code, 302) #Проверка статус кода, при успешном редиректе
        self.assertEqual(response.url, '/polls/welcomepage/') #Проверка корректного редиректа 

    def test_get_restricted(self):
        '''Тест для проверки доступов к страницам пользователей.'''
        get_response = self.client.get('/polls/books/')
        #Проверка редиректа при get запросе на страницу логина
        self.assertEqual(get_response.status_code, 302)
        self.assertEqual(get_response.url, '/polls/login/?next=/polls/books/')
        post_response = self.client.post('/polls/books')
        #Проверка при post запросе
        self.assertEqual(post_response.status_code, 301)

    def test_login_failed(self):
        '''Проверка не правильно введенного пароля'''
        response = self.client.post('/polls/login/', {'username': 'test', 'password': 'wrong'})
        login = self.client.login(username = 'test', password = 'wrong')
        # Проверка статс кода(ошибка не верное введенного пароля выводится в шаблоне)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(login)

class ModelsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_books(self):
        author = models.Author(first_name = 'Автор', last_name = 'Тест', date_of_birth = '2000-01-01')
        author.save()
        publisher = models.Publisher(pub_name = 'Pub')
        publisher.save()
        book = models.Book(title = 'Test', author = author, pub_year = 2022, publisher = publisher)
        book.save()
        book_in_db = models.Book.objects.all()[0]
        self.assertEqual(book, book_in_db)


#Запуск тестов python manage.py test 
# (либо указывать папку с тестами, либо директорую, 
# в которой находится файл с тестом, либо название файла, если не test)