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


@lab4.route('/lab4/zerno', methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template('zerno.html')
    
    grain = request.form['grain']
    weight = request.form['weight']
    
    if not weight:
        message = 'Ошибка: не введен вес'
        return render_template('zerno.html', grain=grain, weight=weight, message=message)
   
    
    prices = {
        'ячмень': 12000,
        'овес': 8500,
        'пшено': 8700,
        'рожь': 14000
    }
    
    total_price = int(weight) * prices[grain]
    zakaz = 'Заказ успешно сформирован. Вы заказали {}. Вес: {} т. Сумма к оплате: {} руб.'.format(grain, weight, int(total_price))

    if int(weight) >= 50 and int(weight) <= 500:
        total_price *= 0.9
        zakaz = 'Заказ успешно сформирован. Вы заказали {}. Вес: {} т. Сумма к оплате: {} руб.'.format(grain, weight, int(total_price)) 
        sk = 'Применена скидка 10% за большой объем'
        return render_template('zerno.html', grain=grain, weight=weight, total_price=total_price, zakaz=zakaz, sk=sk)
    elif int(weight) > 500:
        message = 'Ошибка: такого объема сейчас нет в наличии'
        return render_template('zerno.html', grain=grain, weight=weight, total_price=total_price, message=message)
    elif int(weight) <= 0:
        message = 'Ошибка: неверное значение веса'
        return render_template('zerno.html', grain=grain, weight=weight, total_price=total_price, message=message)
    return render_template('zerno.html', grain=grain, weight=weight, total_price=total_price, zakaz=zakaz)

@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET': 
        return render_template('cookies.html')
    
    color = request.form.get('color')
    
    
    headers = {
        'Set-Cookie': [
            'color=' + color + ';path=/'
            ],
        'Location': '/lab4/cookies'
}

    return '', 303, headers

    

