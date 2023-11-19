from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, Blueprint, session
import psycopg2


lab6 = Blueprint("lab6",__name__)
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

@lab6.route("/lab6")
def main():
    username = session.get("username")
    if not username:
        visibleUser = "Anon"
        return render_template('lab6.html', username=visibleUser)
    return render_template('lab6.html', username=username)