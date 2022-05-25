from django.db import models
from django.core.validators import RegexValidator

class Game(models.Model):
    duration = models.TimeField('Продолжительность игры', validators=[
                                    RegexValidator('[0-9]{2}\:[0-9]{2}\:[0-9]{2}')])
    moves_number = models.PositiveIntegerField('Количество попыток угадывания числа', validators=[
                                    RegexValidator('^[1-9]+[0-9]*')])
    guessing_time = models.DateTimeField('Дата и время окончания игры', validators=[
                                    RegexValidator('[12][0-9]{3}[\.|\/|\-]?((0?[1-9])|(1[0-2]))[\.|\/|\-]?((0?[1-9])|([12]\d)|(3[01]))')])