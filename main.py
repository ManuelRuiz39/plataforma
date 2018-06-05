# -*- coding: utf-8 -*-
__autor__ = "Juan Manuel Ruiz Plascencia"
__version__ = "1.0.1"
__email__ ="maniz39@hotmail.com"
__status__ = "Alpha"
"""
Routes and views for the flask application.
"""
from flask import Flask
from datetime import datetime
from flask import request, redirect, render_template, url_for,session,g,flash,jsonify,make_response
import os,shutil
import bases
import correo
from werkzeug.utils import secure_filename
#from models import Servicios, User
from training import entrena
from chat import platica
import json
app = Flask(__name__)

UPLOAD_FOLDER = '/static/avatar/'
ALLOWED_EXTENSIONS = set(['png','jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Globals

contra = ' '
nom = ''
enc = ' '
lastname = ' '
comp = ' '
cadena = []
y = ''
tipo = ''

#Entrenamiento del bot cada que arranca el servidor
#entrena()

@app.route('/',methods = ['GET','POST'])
def index():
    return render_template('index.html',year=datetime.now().year)
#Login
app.secret_key = os.urandom(24)
@app.route('/login', methods=['POST'])
def login():
    global contra,nom,lastname,comp,enc,tipo
    error = None
    if request.method == 'POST':
        #session.pop('user',None)
        usuario = request.form['username']
        password = request.form['password']
        conexion = bases.iniciar()
        instru = "SELECT * FROM usuarios WHERE email = '"+usuario+"' "
        res = bases.instruccion(conexion,instru)
        for x in res:
            nom = x[1]
            lastname = x[2]
            comp = x[3]
            name = x[4]
            enc = x[5]
            contra = x[7]
            tipo = x[10]
            #print (name,contra)
        if name == usuario and contra == password:
            #print("entro we")
            session['nombre'] = nom 
            session['apellido'] = lastname
            session['compania'] = comp
            session['enc'] = enc
            session['contra'] = contra
            session['usuario'] = usuario
            session['admin'] = tipo
            #flash ('Bienvenido' + nom)
            #jsonify({'code':200,'msg':'Entro','token': name+password})
            if tipo == "admin":
                return admin()
            else:
                return home()
        else:
            flash ('Verifica tu informacion e intenta de nuevo')
            return index()


#Aqui comienza vista cliente
@app.route('/home', methods=['GET'])
def home():
    #if not session.get('usuario'):
    #   return index()
    if not 'usuario' in session:
        return index()
    return render_template('home.html',year=datetime.now().year)

@app.route('/servicios')
def servicios():
    if not 'usuario' in session:
        return index()
    return render_template('servicios.html', year=datetime.now().year)

@app.route('/draas',methods=['GET'])
def draas():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('draas.html',tiempo=tiempo,year=datetime.now().year)
"""
@app.route('/preview')
def preview():
    if not 'usuario' in session:
        return index()
    #agregar categorias como globales para servicios
    categoria = "DRaaS"
    return render_template('preview.html',fecha =datetime.now(),year =datetime.now().year,comp=session['compania'],nom=session['nombre'],lastname=session['apellido'],categoria=categoria)
"""
@app.route('/draas2',methods =['GET','POST'])
def draas2():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    uf = request.form.getlist('uf')
    presupuesto = request.form.getlist('presupuesto')
    autoridad = request.form.getlist('autoridad')
    necesidad = request.form.getlist('necesidad')
    cierre = request.form.getlist('tiempo')
    sername = request.form.getlist('sername')
    hipervisor = request.form.getlist('hipervisor')
    so =  request.form.getlist('so')
    plan = request.form.getlist('plan')
    desc = request.form.getlist('descripcion')
    cpu =  request.form.getlist('cpu')
    ram =  request.form.getlist('ram')
    storage = request.form.getlist('storage')
    storageE = request.form.getlist('storageE')
    tiempo = datetime.now().strftime("%Y-%m-%d")
    can = len(sername)
    for x in range(len(sername)):    
        conexion = bases.iniciar()
        ins = "INSERT INTO `draas` (`nombre`, `hipervisor`,`so`,`criticidad`,`aplicativos`,`cpu`,`ram`,`storageI`,`storageE`,`usuario`,`uf`,`presupuesto`,`autoridad`,`necesidad`,`cierre`) VALUES ('"+sername[x]+"','"+hipervisor[x]+"','"+so[x]+"','"+plan[x]+"','"+desc[x]+"','"+cpu[x]+"','"+ram[x]+"','"+storage[x]+"','"+storageE[x]+"','"+session['usuario']+"','"+uf[x]+"','"+presupuesto[x]+"','"+autoridad[x]+"','"+necesidad[x]+"','"+cierre[x]+"')"
        res = bases.instruccion(conexion,ins)
    return render_template('draas.html',fecha =datetime.now(),tiempo=tiempo,year =datetime.now().year,comp=session['compania'],nom=session['nombre'],lastname=session['apellido'])

@app.route('/baas')
def baas():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('baas.html',year=datetime.now().year,tiempo=tiempo)

@app.route('/baasenv', methods=['POST'])
def baasenv():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    categoria = "DRaaS"
    uf = request.form.getlist('uf')
    presupuesto = request.form.getlist('presupuesto')
    autoridad = request.form.getlist('autoridad')
    necesidad = request.form.getlist('necesidad')
    cierre = request.form.getlist('tiempo')
    sername = request.form.getlist('name')
    so =  request.form.getlist('so')
    hipervisor = request.form.getlist('hipervisor')
    maquinas =  request.form.getlist('maquinas')
    applicativos =  request.form.getlist('aplicativos')
    storage = request.form.getlist('storage')
    can = len(sername)
    for x in range(len(sername)):
        conexion = bases.iniciar()
        ins = "INSERT INTO `baas` (`uf`, `presupuesto`,`autoridad`,`necesidad`,`cierre`,`sername`,`so`,`hipervisor`,`maquinas`,`applicativos`,`storage`) VALUES ('"+uf[x]+"','"+presupuesto[x]+"','"+autoridad[x]+"','"+necesidad[x]+"','"+cierre[x]+"','"+sername[x]+"','"+so[x]+"','"+hipervisor[x]+"','"+maquinas[x]+"','"+applicativos[x]+"','"+storage[x]+"')"
        res = bases.instruccion(conexion,ins)
    return render_template('baas.html',fecha =datetime.now(),tiempo=tiempo,year =datetime.now().year,comp=session['compania'],nom=session['nombre'],lastname=session['apellido'])


@app.route('/monitoreo')
def monitoreo():
    if not 'usuario' in session:
        return index()
    return render_template('monitoreo.html',year=datetime.now().year)

@app.route('/monitoreoSolicitado',methods =['POST'])
def monitoreoSolicitado():
    if not 'usuario' in session:
        return index()
    jsonData = request.get_json()
    #data = str(request.args)
    #jsonData = json.dumps(data)
    return render_template('monitoreo.html',year =datetime.now().year,jsonData = jsonData)

@app.route('/print')
def print():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('print.html',year=datetime.now().year,tiempo = tiempo)

@app.route('/impresion',methods=['POST'])
def impresion():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    razon = request.form['razon']
    categoria = "PRINTaaS"
    ubicacion = request.form['ubicacion']
    ubicaciones = request.form['ubicaciones']
    tiposer = request.form['tiposer']
    cantidad = request.form['cantidad']
    marca = request.form['marca']
    usuarios= request.form['usuarios']
    disponibilidad = request.form['disponibilidad']
    vim = request.form['vim']
    vcm = request.form['vcm']
    vie = request.form['vie']
    color = request.form['color']
    tiemposer = request.form['tiempoServicio']
    software = request.form['softwareAdm']
    equipoColor = request.form['equipoColor']
    tiempo2 = datetime.now().strftime("%Y-%m-%d %H:%M")
    conexion = bases.iniciar()
    ins = "INSERT INTO `printaas` (`razon`, `ubicacion`,`ubicaciones`,`tiposer`,`cantidad`,`marca`,`usuarios`,`disponibilidad`,`vim`,`vcm`,`vie`,`color`,`tiemposer`,`software`,`equipoColor`,`asociado`,`fecha`) VALUES ('"+razon+"','"+ubicacion+"','"+ubicaciones+"','"+tiposer+"','"+cantidad+"','"+marca+"','"+usuarios+"','"+disponibilidad+"','"+vim+"','"+vcm+"','"+vie+"','"+color+"','"+tiemposer+"','"+software+"','"+equipoColor+"','"+session['usuario']+"','"+tiempo2+"')"
    res = bases.instruccion(conexion,ins)
    return render_template('print.html',year=datetime.now().year)

@app.route('/serviciosProfesionales')
def serviciosP():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('serviciosP.html',tiempo=tiempo,year=datetime.now().year)

@app.route('/serviciospro', methods =['POST'])
def serviciospro():
    if not 'usuario' in session:
        return index()
    categoria = "Servicios Profesionales"
    tiempo = datetime.now().strftime("%Y-%m%d")
    uf = request.form['uf']
    presupuesto = request.form['presupuesto']
    autoridad = request.form['autoridad']
    necesidad = request.form['necesidad']
    cierre = request.form['tiempo']
    implementacion = request.form['cate']
    dispositivo = request.form['dispo']
    servicio = request.form['servicio']
    tiempo2 = datetime.now().strftime("%Y-%m-%d %H:%M")
    correo.mensaje(categoria,name)
    conexion = bases.iniciar()
    ins = "INSERT INTO `serviciosprofesionales` (`uf`, `presupuesto`,`autoridad`,`necesidad`,`cierre`,`implementacion`,`dispositivo`,`servicio`,`fecha`,`asociado`) VALUES ('"+uf+"','"+presupuesto+"','"+autoridad+"','"+necesidad+"','"+cierre+"','"+implementacion+"','"+dispositivo+"','"+servicio+"','"+tiempo2+"','"+session['usuario']+"')"
    res = bases.instruccion(conexion,ins)
    return render_template('serviciosP.html',tiempo=tiempo,year =datetime.now().year)

@app.route('/containers')
def containers():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('container.html',year=datetime.now().year,tiempo=tiempo)

@app.route('/containersE',methods =['POST'])
def containersE():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    uf = request.form['uf']
    presupuesto = request.form['presupuesto']
    autoridad = request.form['autoridad']
    necesidad = request.form['necesidad']
    cierre = request.form['tiempo']
    tipo = request.form['tipoR']
    tiempo2 = datetime.now().strftime("%Y-%m-%d %H:%M")
    conexion = bases.iniciar()
    ins = "INSERT INTO `containers` (`uf`, `presupuesto`,`autoridad`,`necesidad`,`requerimiento`,`cierre`,`fecha`,`asociado`) VALUES ('"+uf+"','"+presupuesto+"','"+autoridad+"','"+necesidad+"','"+tipo+"','"+cierre+"','"+tiempo2+"','"+session['usuario']+"')"
    res = bases.instruccion(conexion,ins)
    return render_template('container.html',year=datetime.now().year,tiempo=tiempo)

@app.route('/SECaaS')
def secaas():
    if not 'usuario' in session:
        return index()
    return render_template('secaas.html',year=datetime.now().year)

@app.route('/mesa de ayuda')
def mesaDeAyuda():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('mesaayuda.html',year=datetime.now().year,tiempo=tiempo)

@app.route('/mesaenv', methods =['POST'])
def mesaenv():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    uf = request.form['uf']
    presupuesto = request.form['presupuesto']
    autoridad = request.form['autoridad']
    necesidad = request.form['necesidad']
    cierre = request.form['tiempo']
    atencion = request.form['atencion']
    nivel = request.form['nivel']
    reporte = request.form['reporte']
    tiempo2 = datetime.now().strftime("%Y-%m-%d %H:%M")
    conexion = bases.iniciar()
    ins = "INSERT INTO `mesa` (`uf`, `presupuesto`,`autoridad`,`necesidad`,`requerimiento`,`cierre`,`atencion`,`nivel`,`reporte`,`fecha`,`asociado`) VALUES ('"+uf+"','"+presupuesto+"','"+autoridad+"','"+necesidad+"','"+tipo+"','"+cierre+"','"+atencion+"','"+nivel+"','"+reporte+"','"+tiempo2+"','"+session['usuario']+"')"
    res = bases.instruccion(conexion,ins)
    return render_template('mesaayuda.html',year=datetime.now().year,tiempo=tiempo)

@app.route('/principal')
def principal():
    if not 'usuario' in session:
        return index()
    return render_template('principal.html',year=datetime.now().year)


@app.route('/configuracion',methods = ['GET'])
def configuracion():
    if not 'usuario' in session:
        return index()
    return render_template('configuracion.html',nom = session['nombre'],lastname = session['apellido'],comp = session['compania'],name = session['usuario'],enc = session['enc'],year=datetime.now().year)



@app.route('/config',methods = ['POST'])
def config():
    if not 'usuario' in session:
        return index()
    if request.method == 'POST':
        apass = request.form['pass']
        f = request.files['file']
        #Falta validar que sea el pass actual
        npass = request.form['rpass']
        nom = f.filename 
    #ruta = shutil.move(nom,'/static/avatar/'+nom)
        conexion = bases.iniciar()
        instruc = "UPDATE `usuarios` SET `password` = '"+npass+"' WHERE `email` = '"+name+"';"
        res = bases.instruccion(conexion,instruc)
    return render_template('configuracion.html',nom = session['nombre'],lastname = session['apellido'],comp = session['compania'],name = session['usuario'],enc = enc,year=datetime.now().year)

@app.route('/daas')
def daas():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('daas.html',year =datetime.now().year,tiempo = tiempo)

@app.route('/daasE', methods =['POST'])
def daaasE():
    if not 'usuario' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    uf = request.form['uf']
    presupuesto = request.form['presupuesto']
    autoridad = request.form['autoridad']
    necesidad = request.form['necesidad']
    cierre = request.form['tiempo']

    return render_template('daas.html',year =datetime.now().year,tiempo = tiempo)



@app.route('/herramientas')
def encuestas():
    if not 'usuario' in session:
        return index()
    return render_template('herramientas.html',year=datetime.now().year)

@app.route('/soluciones')
def soluciones():
    if not 'usuario' in session:
        return index()
    return render_template('soluciones.html',year=datetime.now().year)

@app.route('/trabajando')
def trabajo():
    if not 'usuario' in session:
        return index()
    return render_template('trabajo.html',year=datetime.now().year)

@app.route('/contratos')
def contratos():
    if not 'usuario' in session:
        return index()
    return render_template('contratos.html')

@app.route('/seguimiento')
def seguimiento():
    if not 'usuario' in session:
        return index()
    return render_template('seguimiento.html',year=datetime.now().year)

@app.route('/ayuda', methods = ['GET'])
def ayuda():
    if not 'usuario' in session:
        return index()
    return render_template('ayuda.html',year =datetime.now().year,nombre=session['nombre'])

@app.route('/charla', methods =['POST'])
def charla():
    if not 'usuario' in session:
        return index()
    formulario = request.form['text']
    tiempo = datetime.now().strftime("%Y-%m-%d %H:%M")

    humano = (session['nombre'] + " :" + formulario + '\n' )
    texto = platica(formulario)
    yocasta = ("Yocasta :" + texto + '\n' )
    return render_template('conversacion.html',humano = humano,yocasta = yocasta,tiempo = tiempo,year=datetime.now().year)

#Footer
@app.route('/uneteCS')
def altaP():
    return render_template('unete.html')







#Aqui comienza las vistas de administrador
@app.route('/admin')
def admin():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d")
    return render_template('/admin/home.html',year =datetime.now().year,tiempo = tiempo )

@app.route('/registra',methods = ['GET'])
def registra():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    return render_template('/admin/registro.html',year =datetime.now().year)


@app.route('/registrado',methods = ['POST'])
def registrado():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        compania = request.form["compania"]
        mail = request.form["mail"]
        puesto = request.form["puesto"]
        user = request.form["user"]
        password = request.form["pass"]
        #fecha = datetime.now()
        tipo = request.form["tipo"]
        conexion = bases.iniciar()
        inst2 = "INSERT INTO `usuarios` (`nombre`, `apellido`,`compania`,`email`,`puesto`,`usuario`,`password`,`tipo`) VALUES ('"+nombre+"','"+apellido+"','"+compania+"','"+mail+"','"+puesto+"','"+user+"','"+password+"','"+tipo+"')"
        inserta = bases.instruccion(conexion,inst2)

    else:
        print("Algo salio mal")
    return render_template('/admin/registro.html',year =datetime.now().year)

@app.route('/cotizador')
def cotizador():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    conexion =bases.iniciar()
    ins = "SELECT * FROM precios"
    serv = bases.instruccion(conexion,ins)
    return render_template('/admin/cotizador.html',serv = serv,year =datetime.now().year,nom=session['nombre'],comp=session['compania'],lastname=session['apellido'],fecha=datetime.now().strftime("%Y-%m-%d"))

@app.route('/cotizacionpreview',methods=['POST'])
def cotizacionpreview():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    #distribuidor = request.form["distribuidor"]
    #solicitante = request.form["solicitante"]
    #tel = request.form["tel"]
    #mail = request.form["mail"]
    #folio = request.form["folio"]
    servicios = request.get_json()
    #servicio = json.dumps(servicios)
    return render_template('/admin/preview.html',year =datetime.now().year,nom=session['nombre'],comp=session['compania'],lastname=session['apellido'],fecha=datetime.now().strftime("%Y-%m-%d"),servicios=servicios)

@app.route('/serviciosAdm')
def serviciosAdm():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    return render_template('/admin/serviciosAdm.html',year =datetime.now().year)

@app.route('/contratosAdm')
def contratosAdm():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    return render_template('/admin/contratosAdm.html',year =datetime.now().year,fecha=datetime.now().strftime("%Y-%m-%d"))

@app.route('/configuracionAdm')
def configuracionAdm():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    conexion =bases.iniciar()
    ins = "SELECT * FROM usuarios"
    serv = bases.instruccion(conexion,ins)
    return render_template('/admin/configuracionAdm.html',serv =serv,year =datetime.now().year)

@app.route('/eliminaU',methods =['POST'])
def eliminaU():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    mail = request.form["cuenta"]
    conexion = bases.iniciar()
    query =  "DELETE FROM `usuarios` WHERE `id` = '"+mail+"' "
    ejecuta = bases.instruccion(conexion,query)
    conexion2 = bases.iniciar()
    ins = "SELECT * FROM usuarios"
    serv = bases.instruccion(conexion2,ins)  
    return render_template('/admin/configuracionAdm.html',year =datetime.now().year,serv =serv)

@app.route('/supervisa')
def supervisa():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    return render_template('/admin/supervisaBot.html',year =datetime.now().year)

@app.route('/message')
def message():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    return render_template('message.html',year =datetime.now().year)

@app.route('/asociados')
def asociados():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    con = bases.iniciar()
    ins = "SELECT * FROM asociados"
    query = bases.instruccion(con,ins)
    
    return render_template('/admin/asociados.html',query = query,year =datetime.now().year)

@app.route('/proveedores')
def proveedores():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    return render_template('/admin/proveedor.html',year =datetime.now().year)


@app.route('/marketing')
def marketing():
    if not 'usuario' in session and not 'admin' in session:
        return index()
    tiempo = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template('/admin/marketing.html',year =datetime.now().year,tiempo=tiempo)

@app.route('/encuesta/<polls>')
def encuesta(polls):
    return render_template('/admin/demo.html')


#Session
@app.route("/dropsession")
def dropsession():
    #session['usuario'] = False
    session.pop('usuario',None)
    session.clear()
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None
    if 'usuario' in session:
        g.user = session['usuario']

@app.route('/getsession')
def getsession():
    if 'usuario' in session:
        return session['usuario']

    return 'Not logged in!'
"""
@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('index'))  """

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
  app.run()
