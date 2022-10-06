#!/usr/bin/python

'''
Código de Pablo Álvarez Domínguez, 2022
Proyecto UOTA

Generador de diplomas formato PDF

Actualizado por última vez: 06-09-2022
'''

import urllib.request, argparse



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



