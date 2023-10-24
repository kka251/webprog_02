from flask import Blueprint, redirect, url_for, render_template, request
lab4 = Blueprint('lab4',__name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'alex' and password == '123':
        return render_template('success2.html', username=username, password=password)
    
    error = 'Неверные логин и/или пароль'
    if username == '':
        error2 = 'Введите логин'
        return render_template('login.html', error2=error2, username=username, password=password)
    elif password == '':
        error2 = 'Введите пароль'
        return render_template('login.html', error2=error2, username=username, password=password)
        
    return render_template('login.html', error=error, username=username, password=password)
    

@lab4.route('/lab4/success2')
def success2():
    username = request.form.get('username')
    return render_template('success2.html', username=username)


@lab4.route('/lab4/holod', methods = ['GET', 'POST'])
def holod():
    if request.method == 'GET':
        return render_template('holod.html')
    
    temp = request.form.get('temp')
     
    if not temp:
        error3 = 'Ошибка: не задана температура'
        return render_template('holod.html', temp=temp, error3=error3)
    
    temp = int(temp)
    snowflakes = 0
    if temp < -12 :
        error3 = 'Не удалось установить температуру — слишком низкое значение'
        snowflakes = 0
        return render_template('holod.html', temp=temp, error3=error3, snowflakes=snowflakes)
    elif temp > -1 :
        error3 = 'Не удалось установить температуру — слишком высокое значение'
        return render_template('holod.html', temp=temp, error3=error3, snowflakes=snowflakes)
    elif temp >= -12 and temp <= -9:
        error3 = 'Установлена температура: {}'.format(temp) + '°С' 
        snowflakes = 3
        return render_template('holod.html', temp=temp, error3=error3, snowflakes=snowflakes)
    elif temp >= -8 and temp <= -5:
        error3 = 'Установлена температура: {}'.format(temp) + '°С'  
        snowflakes = 2
        return render_template('holod.html', temp=temp, error3=error3, snowflakes=snowflakes)
    elif temp >= -4 and temp <= -1:
        error3 = 'Установлена температура: {}'.format(temp) + '°С' 
        snowflakes = 1
        return render_template('holod.html', temp=temp, error3=error3, snowflakes=snowflakes)
    else:
        return render_template('holod.html', temp=temp, error3=error3, snowflakes=snowflakes)

    