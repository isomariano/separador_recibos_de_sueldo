from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import tabula
import csv
import sys

#funcion que obtiene el numero de legajo de cada recibo y los retorna en una lista
def obtener_legajos(input_recibos, destino):
	try:
		tabula.convert_into(input_recibos, destino, stream=True, output_format="csv", pages="all", area=[135, 35, 150, 75])
	
		legajos=[]
		with open(destino, 'r') as file:
			csv_legajos= csv.reader(file)
			
			for legajo in csv_legajos:
				legajos.append(legajo[0])

		return legajos

	except Exception as e:
		registrar_error("problema al obtener los legajos")
		sys.exit()

#funcion que  genera los pdf de recibo individuales a partir del general
def obtener_recibos_individuales(input_recibos, output_recibos, legajos):
	try:
		with open(input_recibos, "rb") as recibos:
			pdf = PdfFileReader(recibos)
			numero_paginas = pdf.getNumPages()
			indice=0
			paginas_recibo=[]

			for page in range(numero_paginas):  
				output_pdf = PdfFileWriter()
				siguiente_legajo="0"
				if numero_paginas != indice+1:
					siguiente_legajo=legajos[indice+1]

				#identifica si la pagina actual no pertenece al mismo recibo que la siguiente
				if legajos[indice] != siguiente_legajo: 
					paginas_recibo.append(pdf.getPage(page))
					#carga todas las paginas que pertenezcan al recibo
					for pagina in paginas_recibo:
						output_pdf.addPage(pagina)

					nuevo_pdf = (output_recibos+"{}.pdf".format(legajos[indice]))
					with open(nuevo_pdf, "wb") as nuevo:
						output_pdf.write(nuevo)
					paginas_recibo=[]

				#mientras la siguiente pagina sea parte del mismo recibo, la actual se suma a una lista
				else:
					paginas_recibo.append(pdf.getPage(page))

				indice+=1
	except Exception as e:
		registrar_error("problema en la manipulacion del pdf")
		sys.exit()

def start(input_recibos, output_recibos, destino_legajos):

	legajos=obtener_legajos(input_recibos, destino_legajos)

	obtener_recibos_individuales(input_recibos, output_recibos, legajos)