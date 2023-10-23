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
    return render_template('success2.html')