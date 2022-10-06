#!/usr/bin/python

'''
Código de Pablo Álvarez Domínguez, 2022
Proyecto UOTA

Comprobador de si el usuario ganó algún diploma

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
        nombre = "Pepito Pérez" #Nombre del usuario que ganó el diploma
        categoría = 2 # Copiando la estructura de URE; 0: HF, 1: 50MHz, 2: 70MHz, etc.
        color = 0 #0: bronce, 1: plata, 2: oro, 3: platino, 4/5/6: reservado (especiales)
        numeroDiploma = 23 #cuántos diplomas se concedieron en esa categoría y de ese color

        return(indicativo, nombre, categoría, color, número)




'''
class actualizaTablasYDiplomas():

	TODO: Una vez que se subieron los nuevos QSLs, se debe comparar si el usuario obtuvo un diploma 
	(en cuyo caso se avisaría con una notificación y se actualizaría el número de diplomas concedidos
	en esa categoría) y se actualiza la tabla de puntuaciones

'''



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, required=True, help="Indicativo de usuario")

    args = parser.parse_args()

    

if __name__ == "__main__":
    main()
