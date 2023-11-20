from flask import Blueprint, request, render_template, redirect
from db import db
# Данные объекты представляют из себя таблицы users и articles в БД
from db.models import users, articles 
from werkzeug. security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user
import psycopg2

lab6 = Blueprint ("lab6", __name__)

@lab6.route ("/lab6")
def main():
    return render_template('lab6.html')

@lab6.route("/lab6/check")
def check():
# Тоже самое, что select * from users
    my_users = users.query.all()
    print (my_users)
    return "result in console!"

@lab6.route("/lab6/chekarticles")
def chekarticles():
# Тоже самое, что select * from users
    my_articles = articles.query.all()
    print (my_articles)
    return "result in console!"

@lab6.route("/lab6/register2", methods=["GET", "POST"]) 
def register():
    if request.method == "GET":
        return render_template("register2.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    #Проверка на пустое имя
    if not username_form:
        return render_template("register2.html", error="Пустое имя")

    # Проверка на длину пароля
    if len(password_form) < 5:
        return render_template("register2.html", error="Пароль меньше 5-ти символов")

    '''
    Проверяем существование пользователя в БД с таким же именем
    Если такого пользователя нет, то в isUserExist вернется None 
    т.е. мы можем интерпретировать это как False
    '''

    '''
    select * from users
    WHERE username = username form
    LIMIT 1
    -- где username_form - это имя, которое мы получили из формы
    '''

    isUserExist = users.query.filter_by(username=username_form).first()

    # Проверка на существование пользователя
    if isUserExist is not None:
        return render_template ("register2.html", error="Пользователь с таким именем уже существует")
    
    # Хэшируем пароль
    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    # Создаем объект users с нужными полями
    newUser = users(username=username_form, password=hashedPswd)
    # Это INSERT
    db.session.add(newUser)

    # Тоже самое, что и conn. commit ()
    db.session.commit()

    # Перенаправляем на страницу логина
    return redirect("/lab6/log2")

@lab6.route("/lab6/log2", methods=["GET", "POST"])
def log2():
    if request.method == "GET":
        return render_template("log2.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not username_form or not password_form:
        return render_template("log2.html", error="Заполните все поля")

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is None:
        return render_template("log2.html", error="Пользователь не существует")

    if not check_password_hash(my_user.password, password_form):
        return render_template("log2.html", error="Неправильный пароль")

    login_user(my_user, remember=False)
    
    return redirect("/lab6/articles2")

   