from flask import Flask
from flask import render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os

from pymysql import NULL

app = Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='LEj2tGrbzU'
app.config['MYSQL_DATABASE_PASSWORD']='h7Is6gOCSB'
app.config['MYSQL_DATABASE_Db']='LEj2tGrbzU'
mysql.init_app(app)

CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA

@app.route('/')
def index():
    sql="SELECT * FROM `LEj2tGrbzU`.`pacientesvet`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    mascotitas=cursor.fetchall()
    print (mascotitas)
    conn.commit()
    return render_template('pacientes/index.html',mascotitas=mascotitas)

@app.route('/view/<int:id>')
def view(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM LEj2tGrbzU.pacientesvet WHERE id=%s",(id))
    mascotitas=cursor.fetchall()
    conn.commit()
    return render_template('pacientes/view.html',mascotitas=mascotitas)

@app.route('/edit/<int:id>')
def edit(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM pacientesvet.pacientesvet WHERE id=%s",(id))
    mascotitas=cursor.fetchall()
    conn.commit()
    return render_template('pacientes/edit.html',mascotitas=mascotitas)

@app.route('/destroy/<int:id>')
def destroy(id):
    sql="DELETE FROM `pacientesvet`.`pacientesvet` WHERE id=%s;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT foto FROM `pacientesvet`.`pacientesvet` WHERE id=%s",(id))
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
    cursor.execute(sql,id)
    conn.commit()
    return redirect('/')

@app.route("/create")
def create():
    return render_template('pacientes/create.html')

@app.route("/store", methods=['POST'])
def storage():
    _nombre=request.form['nombreForm']
    _especie=request.form['especie']
    _raza=request.form['raza']
    _tamano=request.form['tamano']
    _genero=request.form['genero']
    _peso=request.form['peso']
    _color=request.form['colorForm']
    _fechaNac=request.form['fechaNac']
    _nombreDueno=request.form['nombreDueno']
    _apellidoDueno=request.form['apellidoDueno']
    _direccion=request.form['direccion']
    _tel=request.form['telForm']
    _estado=request.form['estado']
    _foto=request.files['foto']
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    if _foto.filename !='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
    sql="INSERT INTO `LEj2tGrbzU`.`pacientesvet` (`nombreMascota`,`especie`,`raza`,`tamano`,`peso`,`color`,`genero`,`fechaNac`,`estado`,`nombreDueno`,`apellidoDueno`,`direccion`,`telefono`,`foto`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    datos=(_nombre,_especie,_raza,_tamano,_peso,_color,_genero,_fechaNac,_estado,_nombreDueno,_apellidoDueno,_direccion,_tel,nuevoNombreFoto)
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect ('/')

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)

@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['nombreForm']
    _especie=request.form['especie']
    _raza=request.form['raza']
    _tamano=request.form['tamano']
    _genero=request.form['genero']
    _peso=request.form['peso']
    _color=request.form['colorForm']
    _fechaNac=request.form['fechaNac']
    _nombreDueno=request.form['nombreDueno']
    _apellidoDueno=request.form['apellidoDueno']
    _direccion=request.form['direccion']
    _tel=request.form['telForm']
    _estado=request.form['estado']
    _foto=request.files['foto']
    id=request.form['idForm']
    '''now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    if _foto.filename !='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
        cursor.execute("SELECT foto FROM pacientesvet WHERE id=%s",(id))
        fila= cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE pacientesvet SET foto=%s WHERE id=%s",(nuevoNombreFoto,id))
        conn.commit()'''
    sql="UPDATE `pacientesvet`.`pacientesvet` SET `nombreMascota`=%s,`especie`=%s,`raza`=%s,`tamano`=%s,`peso`=%s,`color`=%s,`genero`=%s,`fechaNac`=%s,`estado`=%s,`nombreDueno`=%s,`apellidoDueno`=%s,`direccion`=%s,`telefono`=%s WHERE id=%s;"
    datos=(_nombre,_especie,_raza,_tamano,_peso,_color,_genero,_fechaNac,_estado,_nombreDueno,_apellidoDueno,_direccion,_tel,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)