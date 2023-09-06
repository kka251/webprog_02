from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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

        <footer>
            &copy; Курилова Кристина Александровна, ФБИ14, 3 курс, 2023
        </footer>
    </body>
</html>

"""
