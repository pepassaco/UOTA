#!/usr/bin/python

'''
Código de Pablo Álvarez Domínguez, 2022
Proyecto UOTA

Generador de diplomas formato PDF

Actualizado por última vez: 06-09-2022
'''

import urllib.request, argparse
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics



class APIFran():

	def getArrayIndicativosUnis(self):
		# Devuelve base de datos con los indicativos de las universidades que participan en el diploma
		return(["EA4RCT", "OZ7ORM", "HB9ZZ"])

	def getHistoricoQSLs(self, indicativo):
		return("aqui vendrian los QSOs en JSON")

	def postNuevasQSLs(self, indicativo, QSLs):
		#le mando a la api un stron con los json de los nuevos contactos
		return

	def getDatosDiploma(self, indicativo, IDdip):
		#devuelve la entrada en la base de datos del diploma correspondiente

		indicativo = indicativo #Indicativo del usuario que ganó el diploma
		nombre = "Pepito Pérez Fernández"	#Nombre del usuario que ganó el diploma
		categoría = 0 # Copiando la estructura de URE; 0: HF, 1: 50MHz, 2: 70MHz, etc.
		color = 1 #0: primer qsl, 1: bronce, 2: plata, 3: oro, 4: platino, 5/6/7: reservado (especiales)
		numeroDiploma = 23 #cuántos diplomas se concedieron en esa categoría y de ese color
		fecha = 20220101 #fecha del último QSO necesario para el diploma

		return(indicativo, nombre, categoría, color, numeroDiploma, fecha)




class generaPDFs():

	def __init__(self):
		self.outPDF = "./"


	'''
	def __init__(self, indicativo, nombre, categoría, color, numeroDiploma):
		
		self.indicativo = indicativo
		self.nombre = nombre
		self.categoría = categoría
		self.color = color
		self.numeroDiploma = numeroDiploma
	'''
		
	def generadorDiploma(self, indicativo, nombre, categoría, color, numeroDiploma, fecha):

		f = str(fecha)
		fechaBien = f[0:4]+"/"+f[4:6]+"/"+f[6:8]


		packet = io.BytesIO()
		#can = canvas.Canvas(packet, pagesize=A4)
		can = canvas.Canvas(packet)
		dim = [842, int(842*210/297)]
		can.setPageSize((dim[0], dim[1]))
		fuente = "CS"



		pdfmetrics.registerFont(TTFont(fuente, 'assets/fonts/cs.ttf'))

		medio = [dim[0]/2, dim[1]/2]

		can.setFont(fuente, 62)
		can.drawString(medio[0]-can.stringWidth(indicativo, fuente, 62)/2, medio[1]-20, indicativo)

		
		can.setFont(fuente, 30)
		can.drawString(medio[0]-can.stringWidth(nombre, fuente, 30)/2, medio[1]-90, nombre)

		can.setFont(fuente, 20)
		can.drawString(dim[0]-50-can.stringWidth(indicativo, fuente, 20)/2, dim[1]-100, str(numeroDiploma))

		can.setFont(fuente, 16)
		can.drawString(medio[0]-can.stringWidth(fechaBien, fuente, 16)/2, medio[1]-200, fechaBien)
		can.save()

		
		packet.seek(0)		
		new_pdf = PdfFileReader(packet)	
		existing_pdf = PdfFileReader(open("assets/permanent_awards/"+str(categoría)+"/"+str(color)+".pdf", "rb"))
		output = PdfFileWriter()

		page = existing_pdf.getPage(0)
		page.mergePage(new_pdf.getPage(0))
		output.addPage(page)
		outputStream = open(self.outPDF+"/"+indicativo+"_"+str(categoría)+"_"+str(color)+".pdf", "wb")
		output.write(outputStream)
		outputStream.close()




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, required=True, help="Indicativo de usuario")
    parser.add_argument('-d', type=str, required=True, help="ID (clave primaria) del diploma obtenido")

    args = parser.parse_args()

    miAPI = APIFran()
    [indicativo, nombre, categoría, color, numeroDiploma, fecha] = miAPI.getDatosDiploma(args.i, args.d)

    gPDF =  generaPDFs()
    gPDF.generadorDiploma(indicativo, nombre, categoría, color, numeroDiploma, fecha)

    

    

if __name__ == "__main__":
    main()



