from asset import separar_recibos
from asset.manejo_errores import registrar_error
from asset.manejo_de_rutas import verificar_directorios, obtener_ruta
import os

try:

	verificar_directorios()
	legajos = obtener_ruta("legajos")
	path_input = obtener_ruta("input_recibos")
	input_recibos = os.path.join(path_input, os.listdir(path_input)[0])
	output_recibos = obtener_ruta("output_recibos")

	separar_recibos.start(input_recibos, output_recibos, legajos)

except Exception as e:
	registrar_error("posible error con las carpetas")