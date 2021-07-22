from flask import Flask
from flask import render_template,request,redirect,url_for,flash
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os

app = Flask(__name__)
#app.secret_key="codoacodo21"

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_Db']='pacientesvet'
mysql.init_app(app)

CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA

@app.route('/')
def index():
    sql="SELECT * FROM `pacientesvet`.`pacientesvet`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    mascotitas=cursor.fetchall() 
    print (mascotitas)
    conn.commit()
    return render_template('pacientes/index.html',mascotitas=mascotitas)
@app.route('/destroy/<int:id>')
def destroy(id):
    sql="DELETE FROM `pacientesvet`.`pacientesvet` WHERE id=%s;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,(id))
    conn.commit()
    return redirect('/')

@app.route('/edit', methods=["GET"])
def edit():
    sql="SELECT * FROM `pacientesvet`.`pacientesvet`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    mascotitas=cursor.fetchall()
    print(mascotitas)
    return render_template('pacientes/edit.html',mascotitas=mascotitas)

@app.route("/create")
def create():
    return render_template('pacientes/create.html')
'''
@app.route("/store, methods=['POST']")
def storage():
    _nombre=request.form['nombreForm']
    _id=request.form['idForm']
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
    if _nombre=='' or _especie=='':
        flash('Recuerda llenar estos campos')
        return redirect(url_for('create'))
    if _foto.filename=='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)    
    sql="INSERT INTO `pacientesvet` (`nombreMascota`, `idMascota`, `especie`, `raza`, `tamano`, `peso_actual`, `color`, `genero`, `fechaNac`, `estado`, `nombreDueno`, `apellidoDueno`, `direccion`, `telefono`,`foto`) VALUES (%s,NULL,%s,%s,%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
    datos=(_nombre,_id,_especie,_raza,_tamano,_genero,_peso,_color,_fechaNac,_nombreDueno,_apellidoDueno,_direccion,_tel,_estado,_foto.filename)
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('pacientes/index.html')

@app.route('uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)
'''
@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['nombreForm']
    _id=request.form['idForm']
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
    _tel=request.form['telefono']
    _estado=request.form['estado']
    _foto=request.flies['foto']
    id=request.form['idForm']
    sql ="UPDATE `pacientesvet`SET `nombreMascota`=%s, `idMascota`=%s, `especie`=%s, `raza`=%s, `tamano`=%s, `peso`=%s, `color`=%s, `genero`=%s, `fechaNac`=%s, `estado`=%s, `nombreDueno`=%s, `apellidoDueno`=%s, `direccion`=%s,WHERE `telefono`=%s;"
    datos=(_nombre,_id,_especie,_raza,_tamano,_genero,_peso,_color,_fechaNac,_nombreDueno,_apellidoDueno,_direccion,_tel,_estado,id)
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    if _foto.filename=='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
        cursor.execute("SELECT foto FROM pacientes_mascotas WHERE id=%s", id)
        fila= cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE pacientes_mascotas SET foto=%s WHERE id=%s",(nuevoNombreFoto,id))
        conn.commit()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)