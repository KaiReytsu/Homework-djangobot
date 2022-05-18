from django.db import models
from django.core.validators import RegexValidator

class Author(models.Model):
    first_name = models.CharField('Имя автора', validators=[
                            RegexValidator('^[А-ЯЁ][а-яё]+')],max_length=50)
    last_name = models.CharField('Фамилия автора', validators=[
                            RegexValidator('^[А-ЯЁ][а-яё]+')],max_length=50)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    date_of_death = models.DateField('Дата смерти', validators=[
                                    RegexValidator('((0?[1-9])|([12]\d)|(3[01]))\.((0?[1-9])|(1[0-2]))\.(1[0-9]{3})|(20[01]\d)|(202[0-2])')
                                        ], null=True, blank=True)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Genre(models.Model):
     g_name = models.CharField('Жанр', max_length=50, help_text='Введите жанр книги')
     def __str__(self):
         return self.g_name

class Publisher(models.Model):
    pub_name = models.CharField('Издательство', max_length=50)
    def __str__(self):
        return self.pub_name


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    title = models.CharField('Наименование книги',
                            max_length=50)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    author = models.ForeignKey(Author, verbose_name = 'Автор', on_delete=models.SET_NULL, null=True)
    pub_year = models.PositiveIntegerField('Год публикации', validators=[RegexValidator('(1[0-9]{3})|(20[01]\d)|(202[0-2])')])
    publisher = models.ForeignKey(Publisher, verbose_name = 'Издательство', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(verbose_name='Обложка',upload_to = 'images/', null=True, blank=True)
    def __str__(self):
        return '"%s", %s' %(self.title, self.author)

class Year(models.Model):
    name = models.CharField('Имя', max_length=50)
    year = models.PositiveIntegerField('Год публикации', validators=[RegexValidator('(1[0-9]{3})|(20[01]\d)|(202[0-2])')])
    def __str__(self):
        return self.name

