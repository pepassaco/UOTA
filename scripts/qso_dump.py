#!/usr/bin/python

'''
Código de Pablo Álvarez Domínguez, 2022
Proyecto UOTA

Lector de QSLs electrónicas por medio de las APIs de eQSL y LoTW para su posprocesado y subida a servidor web

Actualizado por última vez: 06-09-2022
'''

import urllib.request, sys, argparse, os
import adif_io




class APIFran():

	def getArrayIndicativosUnis(self):
		# Devuelve base de datos con los indicativos de las universidades que participan en el diploma
		return(["EA4RCT", "OZ7ORM", "HB9ZZ", "EB4ADC"])

	def getHistoricoQSLs(self, indicativo):
		# Devuelve todos las QSLs con universidades ya contabilizadas en un pasado para comparar y no contar repetidas
		QSL1 = {'CALL': 'EB4ADC', 'BAND': '2M', 'BAND_RX': '70CM', 'MODE': 'FM', 'APP_LOTW_MODEGROUP': 'PHONE', 'QSO_DATE': '20210903', 'APP_LOTW_RXQSO': '2021-09-03 22:10:09', 'TIME_ON': '173000', 'APP_LOTW_QSO_TIMESTAMP': '2021-09-03T17:30:00Z', 'PROP_MODE': 'SAT', 'SAT_NAME': 'SO-50', 'QSL_RCVD': 'Y', 'QSLRDATE': '20210911', 'APP_LOTW_RXQSL': '2021-09-11 22:49:11'}
		QSL2 = {'CALL': 'EB4ADC', 'BAND': '2M', 'BAND_RX': '70CM', 'MODE': 'FM', 'APP_LOTW_MODEGROUP': 'PHONE', 'QSO_DATE': '20210801', 'APP_LOTW_RXQSO': '2021-08-01 22:19:05', 'TIME_ON': '202400', 'APP_LOTW_QSO_TIMESTAMP': '2021-08-01T20:24:00Z', 'PROP_MODE': 'SAT', 'SAT_NAME': 'SO-50', 'QSL_RCVD': 'Y', 'QSLRDATE': '20210807', 'APP_LOTW_RXQSL': '2021-08-07 16:45:03'}
		historicoQSLs = [QSL2, QSL1]
		return(historicoQSLs)

	def postNuevasQSLs(self, indicativo, QSLs):
		#le mando a la api un stron con los json de los nuevos contactos
		for qsl in QSLs:
			print(qsl)
			print("\n")
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

		print("ADIF obtenido en eQSL :)\n")


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
			print("ADIF obtenido en LoTW :)\n")






class ADIF2dict():

	def __init__(self):
		self.rutaADIF = "./adiTemp.adi"

	def conversor(self):
		[qsos_raw, adif_header] = adif_io.read_from_file(self.rutaADIF)
		return(qsos_raw)

	def limpiador(self):
		os.remove(self.rutaADIF)





class procesaDict():

	def __init__(self, d, i):
		self.QSLsSubidas = d
		self.indicativo = i

	def comparador(self):

		miAPI = APIFran()
		uniCalls = miAPI.getArrayIndicativosUnis()
		uniQSLs = []

		for qsl in self.QSLsSubidas:

  			if qsl["CALL"] in uniCalls:
  				if "QSO_DATE" in qsl and "MODE" in qsl and "BAND" in qsl:
  					uniQSLs.append(qsl)

		antiguosQSLs = miAPI.getHistoricoQSLs(self.indicativo)
		fechas = []
		modos = []
		bandas = []

		for qsl in antiguosQSLs:
			fechas.append(qsl["QSO_DATE"])
			modos.append(qsl["MODE"])
			bandas.append(qsl["BAND"])



		for i in range(len(antiguosQSLs)):
			qsl = antiguosQSLs[i]

			for qslU in uniQSLs:
				if qslU["QSO_DATE"] in fechas:
					if(qslU["MODE"] == modos[i] and qslU["BAND"] == bandas[i]):
						uniQSLs.remove(qslU)



		miAPI.postNuevasQSLs(self.indicativo, uniQSLs)





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

    a2j = ADIF2dict()
    dictQSO = a2j.conversor()
    #a2j.limpiador()

    pj = procesaDict(dictQSO, args.i)

    pj.comparador()

    

if __name__ == "__main__":
    main()