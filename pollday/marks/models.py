from django.db import models
from django.core.validators import RegexValidator
from django.utils.timezone import now

#2.1 Сделать таблицу оценок студентов с датами. Внешние ключи: студент, предмет.

class Teacher(models.Model):
    '''Модель для преподавателей'''
    teacher_surname = models.CharField('Фамилия преподавателя', validators=[
                            RegexValidator('^[А-ЯЁ][а-яё]+')], max_length=50)
    teacher_name = models.CharField('Имя преподаватель', validators=[
                            RegexValidator('^[А-ЯЁ][а-яё]+')], max_length=50)
    teacher_patronymic = models.CharField('Отчество преподавателя', validators=[
                            RegexValidator('^[А-ЯЁ][а-яё]+')], max_length=50, help_text='Если имеется', null=True, blank=True)

    def __str__(self):
        if self.teacher_patronymic is None:
            return '%s %s.' %(self.teacher_surname, self.teacher_name[0])
        else:
            return '%s %s.%s.' %(self.teacher_surname, self.teacher_name[0], self.teacher_patronymic[0])

class Lesson(models.Model):
    '''Модель для предметов'''
    subject = models.CharField('Предмет', max_length=50)
    teacher = models.ForeignKey(Teacher, verbose_name = 'Преподаватель', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Student(models.Model):
    '''Модель для студентов'''
    surname = models.CharField('Фамилия студента', validators=[
                            RegexValidator('^[А-ЯЁ][а-яё]+')], max_length=50)
    name = models.CharField('Имя студента', validators=[
                            RegexValidator('^[А-ЯЁ][а-яё]+')], max_length=50)

    def __str__(self):
        return '%s %s' %(self.surname, self.name)

class Mark(models.Model):
    '''Модель для оценок за предметы'''
    student = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name='Предмет', on_delete=models.CASCADE)
    grade = models.PositiveIntegerField('Оценка за предмет')
    date = models.DateField('Дата выставления оценки', default=now)

    def __str__(self):
        return '%s получила %s за %s' %(self.student, self.grade, self.lesson)