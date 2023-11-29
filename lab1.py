from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1',__name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)
   

@lab1.route("/menu")
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
                <li>
                    <a href="http://127.0.0.1:5000/lab2" target="_blank" >Лабораторная работа 2</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab3" target="_blank" >Лабораторная работа 3</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab4" target="_blank" >Лабораторная работа 4</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab5" target="_blank" >Лабораторная работа 5</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab6" target="_blank" >Лабораторная работа 6</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab7" target="_blank" >Лабораторная работа 7</a>
                </li>
        </ol>
        <footer>
            &copy; Курилова Кристина Александровна, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>

"""


@lab1.route("/lab1")
def lab():
    return '''
<!DOCTYPE html>
<html>
    <link rel="stylesheet" href = "'''+ url_for('static', filename = 'lab1.css') + '''">
    <head>
        <title> Курилова Кристина Александровна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

            <div>
                Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые бaзовые возможности.
            </div>
            <il >
                <li style="margin: 15px;">
                    <a href="http://127.0.0.1:5000/menu" target="_blank" >МЕНЮ</a>
                </li>
            </il>
        <h2>Реализованные теги</h2>
            <ol>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/oak" target="_blank" >/lab1/oak - дуб</a>
                </li>
                 <li>
                    <a href="http://127.0.0.1:5000/lab1/student" target="_blank" >/lab1/student - студент</a>
                </li>
                 <li>
                    <a href="http://127.0.0.1:5000/lab1/python" target="_blank" >/lab1/python - python</a>
                </li>
                 <li>
                    <a href="http://127.0.0.1:5000/lab1/sm" target="_blank" >/lab1/sm </a>
                </li>
        </ol>
        <footer>
            &copy; Курилова Кристина Александровна, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>

'''


@lab1.route("/lab1/oak")
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


@lab1.route("/lab1/student")
def student():
    return '''
    <!DOCTYPE html>
<html>
    <link rel="stylesheet" href = "'''+ url_for('static', filename = 'lab1.css') + '''">
    <body>
        <h1> Курилова Кристина Александровна</h1>
        <img src="''' + url_for('static', filename='nstu.jpg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/python")
def puthon():
    return '''
    <!DOCTYPE html>
<html>
    <link rel="stylesheet" href = "'''+ url_for('static', filename = 'lab1.css') + '''">
    <body>
        <div>
        Python входит в топ-10 самых востребованных языков программирования и открывает путь в топовые 
        IT-компании: Google, Pixar, Youtube, NASA, Intel, Pinterest используют именно его.</div>

        <div>
        Сильные стороны языка — простота в освоении и низкий порог входа, читабельность, универсальность, 
        большое и активное сообщество. Поэтому Python часто советуют в качестве первого языка начинающим программистам.
        </div>
        <img src="''' + url_for('static', filename='python.jpg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/sm")
def sm():
    return '''
    <!DOCTYPE html>
<html>
    <link rel="stylesheet" href = "'''+ url_for('static', filename = 'lab1.css') + '''">
    <body>
        <div style="text-align: center; background-color: #d4cbcb; margin-left: 0px; "> Простая улыбка может поднять настроение, вызвать положительные эмоции и стать настоящим спасением в сложные периоды.
          Улыбка может передать то, на что порой не способны слова. <p><u>Так почему бы не улыбнуться?</u></p></div>
        <img src="''' + url_for('static', filename='sm.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab2/example')
def example():
    name = 'Курилова Кристина'
    num_lab = 'Лабораторная работа 2'
    group = 'ФБИ-14'
    kurs = '3 курс'
    fruits = [{'name': 'яблоки', 'price': 100},
              {'name': 'груши', 'price': 150}, 
              {'name': 'манго', 'price': 300}, 
              {'name': 'мандарины', 'price': 200}, 
              {'name': 'апельсины', 'price': 250}]
    book = [
        {'author': 'Ф. Достоевский','name': 'Преступление и наказание', 'zhanr': 'роман', 'str': 672 },
        {'author': 'Эрих Фромм','name': 'Бегство от свободы', 'zhanr': 'философия', 'str': 288},
        {'author': 'Эрих Фромм','name': 'Иметь или быть', 'zhanr': 'философия', 'str': 342},
        {'author': 'Карл Юнг','name': 'Психология бессознательного', 'zhanr': 'философия', 'str': 424 },
        {'author': 'Иммануил Кант','name': 'Критика чистого разума', 'zhanr': 'философия', 'str': 330},
        {'author': 'Зигмунд Фрейд','name': 'Введение в психоанализ', 'zhanr': 'психология', 'str': 372},
        {'author': 'Оливер Сакс','name': 'Галлюцинации', 'zhanr': 'психология', 'str': 289},
        {'author': 'Михаил Булгаков','name': 'Мастер и маргарита', 'zhanr': 'роман', 'str': 512 },
        {'author': 'Лев Толстой','name': 'Анна Каренина', 'zhanr': 'роман', 'str': 864 },
        {'author': 'Антон Чехов','name': 'Вишневый сад', 'zhanr': 'пьеса', 'str': 352 }]
    return render_template('example.html', name=name, num_lab=num_lab, group=group, kurs=kurs, fruits=fruits, book=book)


@lab1.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@lab1.route('/lab2/home')
def home():
    return render_template('home.html')