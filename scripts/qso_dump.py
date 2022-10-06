#!/usr/bin/python

'''
Código de Pablo Álvarez Domínguez, 2022
Proyecto UOTA

Lector de QSLs electrónicas por medio de las APIs de eQSL y LoTW para su posprocesado y subida a servidor web

Actualizado por última vez: 06-09-2022
'''

import urllib.request, sys, argparse




class APIFran():

	def getArrayIndicativosUnis(self):
		# Devuelve base de datos con los indicativos de las universidades que participan en el diploma
		return(["EA4RCT", "OZ7ORM", "HB9ZZ"])

	def getHistoricoQSLs(self, indicativo):
		return("aqui vendrian los QSOs en JSON")

	def postNuevasQSLs(self, indicativo, QSLs):
		#le mando a la api un stron con los json de los nuevos contactos
		return

	def getDatosDiploma(self, indicativo, categoría, color):
		#devuelve la entrada en la base de datos del diploma correspondiente

		indicativo = indicativo #Indicativo del usuario que ganó el diploma
		nombre = "Pepito Pérez"	#Nombre del usuario que ganó el diploma
		categoría = 2 # Copiando la estructura de URE; 0: HF, 1: 50MHz, 2: 70MHz, etc.
		color = 0 #0: bronce, 1: plata, 2: oro, 3: platino, 4/5/6: reservado (especiales)
		numeroDiploma = 23 #cuántos diplomas se concedieron en esa categoría y de ese color

		return(indicativo, nombre, categoría, color, número)








class obtenADIF():

	def __init__(self):
		self.rutaADIF = "./adiTemp.adi"

	def getADIFeQSL(self, indicativo, contraseñaeQSL, año = None):

		try:
			if año is None: 
				urlAPI = "https://www.eqsl.cc/qslcard/DownloadInBox.cfm?UserName="+indicativo+"&Password="+contraseñaeQSL+"&RcvdSince=20220901"
			else:
				urlAPI = "https://www.eqsl.cc/qslcard/DownloadInBox.cfm?UserName="+indicativo+"&Password="+contraseñaeQSL+"&RcvdSince="+año+"0101"
		
		except urllib.error.HTTPError:
			print("Error al acceder a eQSL")
			return

		#print(urlAPI, "\n")
		fp = urllib.request.urlopen(urlAPI)
		mybytes = fp.read()
		fp.close()

		mystr = mybytes.decode("utf8")
		posI = mystr.find("../downloadedfiles/")
		posF = mystr.find(".adi\"")
		urlADIF = "https://www.eqsl.cc/"+mystr[posI+3:posF+4]
		
		try:
			urllib.request.urlretrieve(urlADIF, self.rutaADIF)

		except urllib.error.HTTPError:
			print("Error al obtener los datos de eQSL. Revise las credenciales y/o fechas introducidas")
			return

		print("ADIF obtenido en eQSL :)")


	def getADIFLoTW(self, indicativo, contraseñaLoTW, año = None):

		if año is None: 
			urlADIF = "https://lotw.arrl.org/lotwuser/lotwreport.adi?login="+indicativo+"&password="+contraseñaLoTW+"&qso_query=1"+"&qso_qsl=1"
		else:
			urlADIF = "https://lotw.arrl.org/lotwuser/lotwreport.adi?login="+indicativo+"&password="+contraseñaLoTW+"&qso_query=1"+"&qso_qsl=1"+"&qso_startdate="+año+"-01-01"+"&qso_enddate="+str(int(año)+1)+"-01-01"

		fp = urllib.request.urlopen(urlADIF)
		mybytes = fp.read()
		fp.close()

		#print(urlADIF, "\n")
		try:
			urllib.request.urlretrieve(urlADIF, "adiTemp.adi")

		except urllib.error.HTTPError:
			print("Error al obtener los datos de LoTW. Revise las credenciales y/o fechas introducidas")
			return

		cabecera = open(self.rutaADIF, "r").read(14)

		if cabecera == "<!DOCTYPE HTML":
			print("Error al obtener los datos de eQSL. Revise las credenciales y/o fechas introducidas")
		else:
			print("ADIF obtenido en LoTW :)")






class ADIF2JSON():

	def __init__(self):
		self.rutaADIF = "./adiTemp.adi"
		self.rutaJSON = "./adiTemp.json"

	def conversor(self):
		print("TODO")



'''

class procesaJSON():

	def __init__(self):
		self.rutaJSON = "./adiTemp.json"

	def abreJSON(self):
		return("JSON")

	def comparador(self):

		miAPI = APIFran()

		subidasQSLs = self.abreJSON();

		uniQSLs = None

		for #buscamos en miAPI.getArrayIndicativosUnis()

			uniQSLs = #loqsea

		antiguosQSLs = miAPI.getHistoricoQSLs()


		nuevosQSLs = None

		for qso in uniQSLs #comparamos con antiguos

			nuevosQSLs = 

		miAPI.postNuevasQSLs(nuevosQSLs)

'''


'''
class actualizaTablasYDiplomas():

	Una vez que se subieron los nuevos QSLs, se debe comparar si el usuario obtuvo un diploma 
	(en cuyo caso se avisaría con una notificación y se actualizaría el número de diplomas concedidos
	en esa categoría) y se actualiza la tabla de puntuaciones

'''







def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, required=True, help="Indicativo de usuario")
    parser.add_argument('-c', type=str, required=True, help="Contraseña de usuario")
    parser.add_argument('-qsl', type=str, required=True, help="0: eQSL; 1: LoTW")
    parser.add_argument('--fecha', type=str, required=False, help="(Opcional) Filtro por año")

    args = parser.parse_args()

    oa = obtenADIF()

    if int(args.qsl) == 0:
    	oa.getADIFeQSL(args.i, args.c, args.fecha)
    else:
    	oa.getADIFLoTW(args.i, args.c, args.fecha)

    a2j = ADIF2JSON()

    #pj = procesaJSON()

    

if __name__ == "__main__":
    main()
