from django import forms

class Reg_form(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Введите пароль', widget=forms.PasswordInput, help_text='Пожалуйста, потведите введенный пароль')
    age = forms.CharField(label='Возраст', max_length=3)
