from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, Blueprint, session
import psycopg2

lab5 = Blueprint("lab5",__name__)
def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1", 
        database="knowledge_base",
        user= "kristina_knowledge_base",
        password="123")
    
    return conn

def dbClose(cur,conn):
    cur.close()
    conn.close()

@lab5.route("/lab5")
def main():
    username = session.get("username")
    if not username:
        visibleUser = "Anon"
        return render_template('lab5.html', username=visibleUser)
    return render_template('lab5.html', username=username)
    
    
@lab5.route('/lab5/users')
def users():
    conn = dbConnect() 
    cur = conn.cursor()
    
    cur.execute("SELECT username FROM users;")
    users =  cur.fetchall()
    dbClose(cur,conn)
    return render_template('users.html',users=users )

@lab5.route('/lab5/register', methods=["GET","POST"])
def registerPage():
    errors = []

    if request.method == "GET":
        return render_template("register.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors = ["Пожалуйста, заполните все поля"]
        return render_template("register.html", errors=errors)

    hashPassword = generate_password_hash(password)

    conn = dbConnect() 
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s", (username,))

    if cur.fetchone() is not None:
        errors = ["Пользователь с данным именем уже существует"]
        dbClose(cur,conn)
        return render_template("register.html", errors=errors)
    
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashPassword))

    conn.commit()
    conn.close()
    cur.close()

    return redirect("/lab5/log")

@lab5.route('/lab5/log', methods=["GET","POST"])
def loginPage():
    errors = []

    if request.method == "GET":
        return render_template("log.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors = ["Пожалуйста, заполните все поля"]
        return render_template("log.html", errors=errors)

    conn = dbConnect() 
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s", (username,))

    result = cur.fetchone()

    if result is None:
        errors = ["Неправильный логин или пароль"]
        dbClose(cur,conn)
        return render_template("log.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur,conn)
        return redirect("/lab5")
    else:
        errors = ["Неправильный логин или пароль"]
        return render_template("log.html", errors=errors)
    
@lab5.route('/lab5/new_article', methods=["GET","POST"])
def createArticle():
    errors = []

    userID = session.get("id")
    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html")
        if request.method == "POST":
            text_article = request.form.get("text_article")
            tittle = request.form.get("tittle_article")

            if len(text_article) == 0:
                errors = ["Заполните текст"]
                return render_template("new_article.html", errors=errors)
            
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles(user_id, tittle, article_text, is_public) VALUES (%s, %s, %s, %s) RETURNING id",(userID, tittle, text_article, True))

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur,conn)
            return redirect(f"/lab5/article/{new_article_id}")
        return redirect("/lab5/log")

@lab5.route('/lab5/article/<int:article_id>')
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT tittle, article_text FROM articles WHERE id = %s AND is_public = True", (article_id,))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        
        text = articleBody[1].splitlines()

        return render_template("article.html", article_text=text, article_tittle=articleBody[0])
    return render_template(f"/lab5/article/{article_id}")


@lab5.route('/lab5/articles', methods=["GET"])
def userArticles():
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        
        cur.execute("SELECT id, tittle FROM articles WHERE user_id = %s ORDER BY is_favorite ASC, id DESC", (userID,))
        
        articles = cur.fetchall()

        dbClose(cur, conn)

        return render_template("articles.html", articles=articles, username=session.get("username"))

    return redirect("/lab5/log")

@lab5.route('/lab5/logout')
def logout():
    session.clear()  # Удаление всех полей из сессии
    return redirect('/lab5/log')

@lab5.route('/lab5/article/<int:article_id>/favorite', methods=["POST"])
def addToFavorites(article_id):
    userID = session.get("id")
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        cur.execute("UPDATE articles SET is_favorite = True WHERE id = %s AND user_id = %s", (article_id, userID))
        conn.commit()
        dbClose(cur, conn)
        return redirect("/lab5/articles")
    return redirect("/lab5/log")