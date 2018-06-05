#!/usr/bin/python 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage     
    
#Correo de SOM
# som@compusoluciones.com
# 123123Abc
#smtp = outlook.365.com
#993


def mensaje(categoria,name):  
	#emisor = "manizshinigami@gmail.com"
	emisor = "som@compusoluciones.com" 
	receptor = "juruiz@compusoluciones.com"
    # Configuracion del mail 
	html = """\
<html>
<head>
    <meta charset="utf-8" />
    <link rel="shortcut icon" type="image/png" href="https://scontent.fgdl3-1.fna.fbcdn.net/v/t1.0-1/p50x50/12734268_1063128193753865_1013925773745150687_n.png?oh=f38f57707ea2d7346a7f951b96bbac65&oe=5AD08BC7" />
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-amber.min.css" />
    <!--<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">-->
    <!-- Material Design icon font -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js"></script>
</head>
<body>
    <div class="container" style="text-align:center;font-family:'News Gothic'">
        <div class="container">
            <img src="http://mkt.compusoluciones.com/e/ConstantContact/SOM/placa.png" style="width:auto; height:auto; text-align:center;align-items:center;justify-content:center" />
        </div>
        <div >
            <h1 style="color:#0074c7">Oportunidad de """+categoria+"""</h1>
        </div>
        <hr />
        <div style="font-family:'News Gothic';font-size:medium">
            Ha sido solicitado el servicio de la soluci&oacute;n """+categoria+"""   por el asociado """+name+"""  .<br />
            Sus datos son los siguientes:<br />
        </div>
        <hr />
    </div>
</body>
</html>
"""
	mensajeHtml = MIMEText(html, 'html')
    

	mensaje = MIMEMultipart('alternative')
	mensaje['From']= emisor 
	mensaje['To']=receptor 
	mensaje['Subject']="Plataforma SOM"
	mensaje.attach(mensajeHtml)
    
	fp = open('placa.png', 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()

	# Define the image's ID as referenced above
	msgImage.add_header('Content-ID', '<image1>')
	mensaje.attach(msgImage)
   # Nos conectamos al servidor SMTP de Gmail 
	serverSMTP = smtplib.SMTP('outlook.office365.com',587) 
	serverSMTP.ehlo() 
	serverSMTP.starttls() 
	serverSMTP.ehlo() 
	serverSMTP.login(emisor,"123123Abc") 
   
    # Enviamos el mensaje 
	serverSMTP.sendmail(emisor,receptor,mensaje.as_string()) 
    
    # Cerramos la conexion 
	serverSMTP.close()


#mensaje()
