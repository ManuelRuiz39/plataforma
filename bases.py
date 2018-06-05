import MySQLdb
 
DB_HOST = '127.0.0.1' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'som'

db = ""

#Se utliza para conectar y crear el cursor en una sola funcion
def iniciar():
	global db
	db = conectar()
	cursor = crear_cursor(db)
	return cursor

#Devuelve la conexion de Mysql
def conectar():
	try:
		db = MySQLdb.connect(host=DB_HOST, user=DB_USER,passwd=DB_PASS, db=DB_NAME)
		return db
	except:
		print("Error al conectar a MySql")

def desconectar():
    global db
    db.close()

#Crear el objeto para realizar consultas mysql
def crear_cursor(db):
	try:
		cursor = db.cursor()
		return cursor
	except:
		print("Error al crear el cursor")

#Realiza la consulta mysql select y devuelve una lista
def instruccion(conexion,instruccion):
	global db
	try:
		if(instruccion.lower().find("select") > -1 or instruccion.lower().find("show") > -1):
			conexion.execute(instruccion)
			return list(conexion)
		elif(instruccion.lower().find("insert") > -1 or instruccion.lower().find("update") > -1 or instruccion.lower().find("delete") > -1):
			try:
				rest = conexion.execute(instruccion)
				db.commit()
				if(rest == 1):
					return True
				else:
					return False
			except:
				db.rollback()
				return False	
		else:
			return False
	except:
		return False

#Realiza una consulta select y si se agrega la lista de parametros se realiza
#	una busqueda; lista = "[('campo1','LIKE','%dato_a_buscar%'),('campo2','=','dato_a_buscar2')]"

def select(conexion,tabla,inst):
	inst2 = "SHOW COLUMNS FROM "+tabla
	columnas = instruccion(conexion,inst2)
	consulta = instruccion(conexion,inst)
	tabla = []
	for x in consulta:
		con = 0
		dic = {}
		for y in x:
			dic[columnas[con][0]] = y
			con += 1
		tabla.append(dic)

	return tabla

"""
inst = "SELECT * FROM prueba1 WHERE dato1 = 1"
inst2 = "INSERT INTO `prueba1` (`id`, `dato1`) VALUES (NULL, '50')"
inst3 = "DELETE FROM `prueba1` WHERE `prueba1`.`id` = 6"
inst4 = "UPDATE `prueba1` SET `dato1` = '10' WHERE `prueba1`.`id` = 2;"
inst5 = "SHOW COLUMNS FROM prueba1" 

conexion = iniciar()
con1 = select(conexion,"prueba1",inst)
print(con1)
"""