from flask import request
from flask_package import app
from flask_package.db import mysql

@app.route('/insert', methods= ['POST'])
def insert():
    nim = request.form['nim']
    nama = request.form['nama']
    alamat = request.form['alamat']
    fakultas = request.form['fakultas']
    prodi = request.form['prodi']
    jenjang = request.form['jenjang']
    kelas = request.form['kelas']
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO mahasiswa VALUES(%s,%s,%s,%s,%s,%s,%s)''',
                   (nim,nama,alamat,fakultas,prodi,jenjang,kelas))
    mysql.connection.commit()
    cursor.close()
    return f"Done!"
