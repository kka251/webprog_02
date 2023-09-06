from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")

@app.route("/index")
def start():
    return redirect ("/menu", code=302)
   

@app.route("/menu")
def menu():
     return """
<!DOCTYPE html>
<html>
    <head>
        <tittle> НГТУ, ФБ, Лабораторные работы<tittle>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1> web-сервер на flask</h1>

        <ol>
                <li>
                    <a href="http://127.0.0.1:5000/lab1" target="_blank" >Лабораторная работа 1</a>
                </li>
        </ol>
        <footer>
            &copy; Курилова Кристина Александровна, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>

"""
@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html>
    <head>
        <tittle>Курилова Кристина Александровна, лабораторная 1<tittle>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1> web-сервер на flask</h1>
            <div>
                Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые бaзовые возможности.
            </div>
        <footer>
            &copy; Курилова Кристина Александровна, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>

"""

@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href = "'''+ url_for('static', filename = 'lab1.css') + '''">
    <body>
        <h1> Дуб </h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''