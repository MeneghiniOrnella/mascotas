from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
mysql.init_app(app)

CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA

@app.route("/uploads/<nombreFoto>")
def uploads(nombreFoto):
    

@app.route('/')
def index():
    sql ="INSERT INTO `pacientesvet` (`nombre_mascota`, `id_mascota`, `especie`, `raza`, `tamaño`, `peso_actual`, `color`, `genero`, `fecha_nac`, `estado`, `vacunas_dadas`, `nombre_dueño`, `apellido_dueño`, `direccion`, `telefono`, `fecha_defuncion`) VALUES ('Luna', '1', 'perro', '.', 'grande', '29', 'dorado', 'hembra', '2018-02-14', 'sano', '15', 'adriana', 'adriluna', 'Luna 1200, CABA', '1122558855', '.');"
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('templates/index.html')

@app.route('/destroy/<int:id>')
def destroy(id):
    conn= mysql.connect()
    cursor= conn.cursor()
    
    cursor.execute("SELECT foto FROM pacientes_mascotas WHERE id=%s", id)
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
    
    cursor.execute("DELETE FROM pacientes_mascotas WHERE id=%s", (id))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit():
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute("SELECT FROM pacientes_mascotas WHERE id=%s", (id))
    mascotitas=cursor.fetchall()
    conn.commit()
    print(mascotitas)
    return render_template('templates/edit.html',mascotitas=mascotitas)

@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['nombreForm']
    _id=request.form['idForm']
    _especie=request.form['especie']
    _raza=request.form['raza']
    _tamaño=request.form['tamaño']
    _genero=request.form['genero']
    _peso=request.form['peso']
    _color=request.form['colorForm']
    _fechaNac=request.form['fechaNac']
    _nombreDueño=request.form['nombreDueño']
    _apellidoDueño=request.form['apellidoDueño']
    _direccion=request.form['direccion']
    _tel=request.form['tel']
    _estado=request.form['estado']
    _foto=request.flies['foto']
    _fechaFin=request.form['fechaFin']
    id=request.form['idForm']

    sql ="UPDATE `pacientesvet`SET `nombre_mascota`=%s, `id_mascota`=%s, `especie`=%s, `raza`=%s, `tamaño`=%s, `peso_actual`=%s, `color`=%s, `genero`=%s, `fecha_nac`=%s, `estado`=%s, `vacunas_dadas`=%s, `nombre_dueño`=%s, `apellido_dueño`=%s, `direccion`=%s, `telefono`=%s,WHERE `fecha_defuncion`=%s;"
    
    datos=(_nombre,_id,_especie,_raza,_tamaño,_genero,_peso,_color,_fechaNac,_nombreDueño,_apellidoDueño,_direccion,_tel,_estado,id,_fechaFin)
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    if _foto.filename='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
        cursor.execute("SELECT foto FROM pacientes_mascotas WHERE id=%s", id)
        fila= cursor.fetchall()

        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE pacientes_mascotas SET foto=%s WHERE id=%s",(nuevoNombreFoto,id))
        conn.commit()

    return redirect('/')

@app.route("/create")
def create(id):
    return render_template('templates/create.html')

@app.route("/connect, methods=['POST']")
def storage():
    _nombre=request.form['nombreForm']
    _id=request.form['idForm']
    _especie=request.form['especie']
    _raza=request.form['raza']
    _tamaño=request.form['tamaño']
    _genero=request.form['genero']
    _peso=request.form['peso']
    _color=request.form['colorForm']
    _fechaNac=request.form['fechaNac']
    _nombreDueño=request.form['nombreDueño']
    _apellidoDueño=request.form['apellidoDueño']
    _direccion=request.form['direccion']
    _tel=request.form['tel']
    _estado=request.form['estado']
    _foto=request.flies['foto']
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    if _foto.filename='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)
    _fechaFin=request.form['fechaFin']
    
    sql ="INSERT INTO `pacientesvet` (`nombre_mascota`, `id_mascota`, `especie`, `raza`, `tamaño`, `peso_actual`, `color`, `genero`, `fecha_nac`, `estado`, `vacunas_dadas`, `nombre_dueño`, `apellido_dueño`, `direccion`, `telefono`, `fecha_defuncion`) VALUES (%s, NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    
    datos=(_nombre,_id,_especie,_raza,_tamaño,_genero,_peso,_color,_fechaNac,_nombreDueño,_apellidoDueño,_direccion,_tel,_estado,_foto.filename,_fechaFin)
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql)
    mascotas=cursor.fetchall()
    print(mascotas)
    conn.commit()
    return redirect('/')

'''from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('templates/index.html')

if __name__== '__main__':
    app.run(debug=True)'''

