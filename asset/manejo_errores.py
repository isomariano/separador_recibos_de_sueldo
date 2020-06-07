import os

def registrar_error(error):
	ruta=os.path.join(os.getcwd(), r"output_recibos\error.txt")

	with open(ruta, "w") as registro_error:
		registro_error.write(error)
