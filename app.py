from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)

@app.route('/lab2/example')
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


@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@app.route('/lab2/home')
def home():
    return render_template('home.html')