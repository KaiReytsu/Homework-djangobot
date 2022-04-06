from django import forms

class LoginFrom(forms.Form):
    '''Форма для логина'''
    #т.к. наименование переменной поступает в html 
    #попробовала назвать переменные по русски, 
    #проверить, будет ли ошибка
    логин = forms.CharField()                       
    пароль = forms.CharField(widget = forms.PasswordInput)
