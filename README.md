# Homework-djangobot

#### Перед запуском проекта нужно создать secret key

```
touch pollday/pollday/secrets.py
```
#### В файл добавить:
```
SECRET_KEY = 'your secret key'
```
####  Для запуска тестов:
```
python3 manage.py test tests
```
#### Файл .env.example скопировать как .env
#### В файле нужно указать имя базы данных, юзера и пароль.
#### При необходимости, адрес базы данных в .env можно изменить
#### Для работы проекта база данных должна быть запущена