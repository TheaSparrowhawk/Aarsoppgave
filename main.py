from flask import Flask, request, render_template

import mysql.connector


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hei på deg</h1>'


@app.route('/nyside')
def nyside() -> 'str': #bare for lesbarhet
    return '<h1>nyside</h1>'


@app.route('/login')
def login():
    return '''<form method = "POST" action = "sende-data">
              <input type = "text" name = "fornavn" />
              <input type = "submit" value = "submit" />
              </form>'''


@app.route('/sende-data', methods=['POST'])
def motta(): 
    fornavn = request.form['fornavn']

    mydb = mysql.connector.connect(
        host="192.168.106.211",
        user="admin",
        password="passy",
        database="flaskedb"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO bruker (fornavn) VALUES (%s)"
    val = ([fornavn])
    mycursor.execute(sql, val)

    return 'satte inn bruker ' + fornavn

@app.route('/htmleks')
def htmleks():
    return render_template('eple.html')

if __name__ == '__main__':
    app.run(debug=True)



