from flask import Blueprint, request, render_template, redirect, session, url_for, abort

lab8 = Blueprint ("lab8", __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')