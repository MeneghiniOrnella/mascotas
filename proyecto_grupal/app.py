from flask import Flask
from flask import render_template,request
from flaskext.mysql import MySQL
from datetime import datetime

app= Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
mysql.init_app(app)

@app.route('/')
def index():
    sql ="INSERT INTO `pacientesvet` (`nombre_mascota`, `id_mascota`, `especie`, `raza`, `tamaño`, `peso_actual`, `color`, `genero`, `fecha_nac`, `estado`, `vacunas_dadas`, `nombre_dueño`, `apellido_dueño`, `direccion`, `telefono`, `fecha_defuncion`) VALUES ('Luna', '1', 'perro', '', 'grande', '29', 'dorado', 'hembra', '2018-02-14', 'sano', '15', 'adriana', 'adriluna', 'Luna 1200, CABA', '1122558855', '');"
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('templates\index.html')

@app.route("/create")
def create():
    return render_template('templates\create.html')

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
    _fechaFin=request.form['fechaFin']
    sql ="INSERT INTO `pacientesvet` (`nombre_mascota`, `id_mascota`, `especie`, `raza`, `tamaño`, `peso_actual`, `color`, `genero`, `fecha_nac`, `estado`, `vacunas_dadas`, `nombre_dueño`, `apellido_dueño`, `direccion`, `telefono`, `fecha_defuncion`) VALUES (%s, NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    datos=(_nombre,_id,_especie,_raza,_tamaño,_genero,_peso,_color,_fechaNac,_nombreDueño,_apellidoDueño,_direccion,_tel,_estado,_foto.filename,_fechaFin)
    conn= mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('templates/index.html')


if __name__== '__main__':
    app.run(debug=True)

