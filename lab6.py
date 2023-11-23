from flask import Blueprint, request, render_template, redirect, session, url_for
from db import db
# Данные объекты представляют из себя таблицы users и articles в БД
from db.models import users, articles 
from werkzeug. security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
import psycopg2

lab6 = Blueprint ("lab6", __name__)

@lab6.route("/lab6")
def main():
    if current_user.is_authenticated:
        visibleUser = current_user.username  # Получите имя текущего пользователя
    else:
        visibleUser = "Аноним"

    return render_template('lab6.html', username_form=visibleUser)

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
    
    return redirect("/lab6")

@lab6.route("/lab6/articles2")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template("list_articles.html", articles=my_articles)

@lab6.route("/lab6/logout2")
@login_required
def logout():
    logout_user()
    return redirect("/lab6")

@lab6.route("/lab6/add_article", methods=["GET", "POST"])
@login_required
def add_article():
    if request.method == "POST":
    # Проверка на пустое название статьи
        tittle = request.form.get("tittle")
        article_text = request.form.get("article_text")
        if tittle and article_text:  # Проверка, что title и article_text не пустые
            new_article = articles(tittle=tittle, article_text=article_text, user_id=current_user.id, is_public=True)
            db.session.add(new_article)
            db.session.commit()
            return redirect(url_for('lab6.list_articles'))
        else:
            return render_template("add_article.html", error="Заполните все поля!")
    return render_template("add_article.html")


@lab6.route ("/lab6/articles2/<int:article_id>", methods=["GET"])
@login_required 
def getArticle(article_id):
    article = articles.query.filter_by(id=article_id).first()
    if article:
        return render_template("articles2.html", article=article)
    else:
        return "Not found!"

@lab6.route("/lab6/list_articles", methods=["GET"])
@login_required 
def list_articles():
    my_articles = articles.query.order_by(articles.is_favorite.asc()).all()
    return render_template('list_articles.html', articles=my_articles)

@lab6.route("/lab6/add_to_favorites/<int:article_id>", methods=["POST"])
@login_required
def add_to_favorites(article_id):
    article = articles.query.filter_by(id=article_id).first()
    if article:
        article.is_favorite = True
        db.session.commit()
    return redirect(url_for('lab6.list_articles'))

@lab6.route("/lab6/like_article/<int:article_id>", methods=["POST"])
@login_required
def like_article(article_id):
    article = articles.query.get(article_id)
    if article:
        article.likes = article.likes + 1 if article.likes else 1
        db.session.commit()
    return redirect(url_for('lab6.getArticle', article_id=article_id))