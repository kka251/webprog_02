from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee' :
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30

    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    return render_template('success.html')

@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    fio = request.args.get('fio')
    if fio == '':
        errors['fio'] = 'Заполните поле!'
    tip = request.args.get('tip')
    polka = request.args.get('polka')
    bag = request.args.get('bag')
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    viezd = request.args.get('viezd')
    if viezd == '':
        errors['viezd'] = 'Заполните поле!'
    prib = request.args.get('prib')
    if prib == '':
        errors['prib'] = 'Заполните поле!'
    date = request.args.get('date')
    if prib == '':
        errors['date'] = 'Заполните поле!'
    return render_template('ticket.html', fio=fio, age=age, tip=tip, polka=polka, bag=bag, viezd=viezd, prib=prib, date=date, errors=errors)

@lab3.route('/lab3/oform')
def oform():
    fio = request.args.get('fio')
    tip = request.args.get('tip')
    polka = request.args.get('polka')
    bag = request.args.get('bag')
    age = request.args.get('age')
    viezd = request.args.get('viezd')
    prib = request.args.get('prib')
    date = request.args.get('date')
    return render_template('oform.html', fio=fio, age=age, tip=tip, polka=polka, bag=bag, viezd=viezd, prib=prib, date=date)

@lab3.route('/lab3/pay2')
def pay2():
    price2 = 1500
    if request.args.get('bag') == 'yes':
        price2 += 500
    
    return render_template('pay2.html', price2=price2)