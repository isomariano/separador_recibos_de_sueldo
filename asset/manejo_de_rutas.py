#modulo para menejo de rutas
import os

#creacion de las carpetas necesarias, en caso de no encontrarse presentes
def verificar_directorios():
	directorios=["input_recibos", "output_recibos", "legajos"]
	for directorio in directorios:
		if not os.path.exists(directorio):
			os.makedirs(os.path.join(os.getcwd(), directorio))

def obtener_ruta(param):
	path_config=os.path.join(os.getcwd(), "config.ini")

	with open(path_config) as archivo:
		lineas = archivo.readlines()

		for linea in lineas:
			partes = linea.split("=")
			if partes[0] == param:
				ruta=os.path.join(os.getcwd(), partes[1]).strip()

				return ruta
	return False
