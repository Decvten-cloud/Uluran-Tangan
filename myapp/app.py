from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static')

# Database configuration
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "donation"  # Nama database dari file phpMyAdmin Anda
mysql = MySQL(app)
app.secret_key = 'secret'

from myapp.controllers.controller import (
    beranda as ix,
    daftar as reg,
    login as log,
    donasikonten1 as don1,
    logout as lo,
    get_profil,
    donasikonten2 as don2,
    donasikonten3 as don3,
    donasikonten4 as don4,
    donasikonten5 as don5,
    donasikonten6 as don6,
    donasikonten7 as don7,
    donasikonten8 as don8,
    donasikonten9 as don9
)


@app.route('/', methods=['GET', 'POST'])
def beranda():
    return ix()


@app.route('/register', methods=['GET', 'POST'])
def daftar():
    return reg()


@app.route('/login', methods=['GET', 'POST'])
def login():
    return log()

@app.route('/logout')
def logout():
    return lo()

@app.route('/donasi', methods=['GET'] )
def donasi():
    return render_template('donasi.html')

@app.route('/tentang_kami', methods=['GET'] )
def tentang_kami():
    return render_template('tentang_kami.html')

@app.route('/profil', methods=['GET'] )
def profil():
    return get_profil()



@app.route('/donasikonten1', methods=['GET', 'POST'] )
def donasikonten1():
    return don1()

@app.route('/donasikonten2', methods=['GET', 'POST'] )
def donasikonten2():
    return don2()

@app.route('/donasikonten3', methods=['GET', 'POST'] )
def donasikonten3():
    return don3()

@app.route('/donasikonten4', methods=['GET', 'POST'] )
def donasikonten4():
    return don4()

@app.route('/donasikonten5', methods=['GET', 'POST'] )
def donasikonten5():
    return don5()

@app.route('/donasikonten6', methods=['GET', 'POST'] )
def donasikonten6():
    return don6()

@app.route('/donasikonten7', methods=['GET', 'POST'] )
def donasikonten7():
    return don7()

@app.route('/donasikonten8', methods=['GET', 'POST'] )
def donasikonten8():
    return don8()

@app.route('/donasikonten9', methods=['GET', 'POST'] )
def donasikonten9():
    return don9()


@app.route('/konten1', methods=['GET', 'POST'] )
def konten1():
    return render_template('konten1.html')

@app.route('/konten2', methods=['GET', 'POST'] )
def konten2():
    return render_template('konten2.html')

@app.route('/konten3', methods=['GET', 'POST'] )
def konten3():
    return render_template('konten3.html')

@app.route('/konten4', methods=['GET', 'POST'] )
def konten4():
    return render_template('konten4.html')

@app.route('/konten5', methods=['GET', 'POST'] )
def konten5():
    return render_template('konten5.html')

@app.route('/konten6', methods=['GET', 'POST'] )
def konten6():
    return render_template('konten6.html')

@app.route('/konten7', methods=['GET', 'POST'] )
def konten7():
    return render_template('konten7.html')

@app.route('/konten8', methods=['GET', 'POST'] )
def konten8():
    return render_template('konten8.html')

@app.route('/konten9', methods=['GET', 'POST'] )
def konten9():
    return render_template('konten9.html')




if __name__ == '__main__':
    app.run(debug=True)
