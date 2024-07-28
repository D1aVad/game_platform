from django.shortcuts import render
from .forms import Reg_form
from django.http import HttpResponse
import sqlite3

connection = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = connection.cursor()

users = {}
cursor.execute(''' 

CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password INTEGER,
age INTEGER NOT NULL
)
''')
cursor.execute("SELECT username FROM Users")
users_rest = cursor.fetchall()
print(users_rest)

def search(data, target):
    for i in range(len(data)):
            if target in data[i]:
                return True
    return False
    

def index(request):
    if request.method == 'POST':
        form = Reg_form(request.POST)
        condition = False
        age_no = False
        user_no = False
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            
            if password != repeat_password:
                condition = True
                context = {
                    'condition' : condition
                }
                # Возвращаем ответ с текстом в виде HTML, если условие истинно
                return render(request, 'fifth_task/registration_page.html', context)
            elif int(age) < 18:
                age_no = True
                context = {
                    'age_no' : age_no
                }
                # Возвращаем ответ с текстом в виде HTML, если условие истинно
                return render(request, 'fifth_task/registration_page.html', context)
            elif search(users_rest, username):
                user_no = True
                context = {
                    'user_no' : user_no
                }
                # Возвращаем ответ с текстом в виде HTML, если условие истинно
                return render(request, 'fifth_task/registration_page.html', context)
            else:
                #users[username] = [password, age]
                #print(users)
                cursor.execute("INSERT INTO Users(username, password, age) VALUES (?, ?, ?)", (username, password, age))
                connection.commit()


                

                

    else:
        form = Reg_form()
    return render(request, 'fifth_task/registration_page.html', {'form': form})
# Create your views here.
