#!/usr/bin/python

'''
Código de Pablo Álvarez Domínguez, 2022
Proyecto UOTA

Comprobador de si el usuario ganó algún diploma

Actualizado por última vez: 06-09-2022
'''


import urllib.request, sys, argparse, os
import adif_io
from numpy import zeros

class APIFran():

    def getArrayIndicativosUnis(self):
        # Devuelve base de datos con los indicativos de las universidades que participan en el diploma
        return(["EA4RCT", "OZ7ORM", "HB9ZZ", "EB4ADC"])

    def getHistoricoQSLs(self, indicativo):
        # Devuelve todos las QSLs con universidades ya contabilizadas en un pasado para comparar y no contar repetidas
        QSL1 = {'CALL': 'EB4ADC', 'BAND': '2M', 'BAND_RX': '70CM', 'MODE': 'FM', 'APP_LOTW_MODEGROUP': 'PHONE', 'QSO_DATE': '20210903', 'APP_LOTW_RXQSO': '2021-09-03 22:10:09', 'TIME_ON': '173000', 'APP_LOTW_QSO_TIMESTAMP': '2021-09-03T17:30:00Z', 'PROP_MODE': 'SAT', 'SAT_NAME': 'SO-50', 'QSL_RCVD': 'Y', 'QSLRDATE': '20210911', 'APP_LOTW_RXQSL': '2021-09-11 22:49:11'}
        QSL2 = {'CALL': 'HB9ZZ', 'BAND': '2M', 'BAND_RX': '70CM', 'MODE': 'FM', 'APP_LOTW_MODEGROUP': 'PHONE', 'QSO_DATE': '20210801', 'APP_LOTW_RXQSO': '2021-08-01 22:19:05', 'TIME_ON': '202400', 'APP_LOTW_QSO_TIMESTAMP': '2021-08-01T20:24:00Z', 'SAT_NAME': 'SO-50', 'QSL_RCVD': 'Y', 'QSLRDATE': '20210807', 'APP_LOTW_RXQSL': '2021-08-07 16:45:03'}
        QSL3 = {'CALL': 'OZ7ORM', 'BAND': '2M', 'BAND_RX': '70CM', 'MODE': 'FM', 'APP_LOTW_MODEGROUP': 'PHONE', 'QSO_DATE': '20210801', 'APP_LOTW_RXQSO': '2021-08-01 22:19:05', 'TIME_ON': '202400', 'APP_LOTW_QSO_TIMESTAMP': '2021-08-01T20:24:00Z', 'PROP_MODE': 'SAT', 'SAT_NAME': 'SO-50', 'QSL_RCVD': 'Y', 'QSLRDATE': '20210807', 'APP_LOTW_RXQSL': '2021-08-07 16:45:03'}
        historicoQSLs = [QSL2, QSL1, QSL3]
        return(historicoQSLs)

    def postNuevasQSLs(self, indicativo, QSLs):
        #le mando a la api un stron con los json de los nuevos contactos
        for qsl in QSLs:
            print(qsl)
            print("\n")
        return

    def getDatosDiploma(self, indicativo, IDdip):
        #devuelve la entrada en la base de datos del diploma correspondiente

        indicativo = indicativo #Indicativo del usuario que ganó el diploma
        nombre = "Pepito Pérez Fernández"   #Nombre del usuario que ganó el diploma
        categoría = 0 # Copiando la estructura de URE; 0: HF, 1: 50MHz, 2: 70MHz, etc.
        color = 1 #0: primer qsl, 1: bronce, 2: plata, 3: oro, 4: platino, 5/6/7: reservado (especiales)
        numeroDiploma = 23 #cuántos diplomas se concedieron en esa categoría y de ese color
        fecha = 20220101 #fecha del último QSO necesario para el diploma

        return(indicativo, nombre, categoría, color, numeroDiploma, fecha)

    def postNuevosDiplomas(self, indicativo, updatedDip):

        #Se le manda un array actualizado con los diplomas obtenidos por ese indicativo (true=diploma, false=pringado,
        #cada fila es una categoría y cada columna un color)

        #Ejemplo para alguien que tiene 1 QSO en 2m y 2 QSOs en SAT
        
        print(updatedDip)
        print("\n:)\n")
        return






class actualizador():

    '''
	TODO: Una vez que se subieron los nuevos QSLs, se debe comparar si el usuario obtuvo un diploma 
	(en cuyo caso se avisaría con una notificación y se actualizaría el número de diplomas concedidos
	en esa categoría)
    '''

    def __init__(self):
                        # HF, 6m, 4m, 2m, 70cm, 23cm, uW, SAT, EME, MS
        self.QSLsPlat =  [10,  4,  2,  4,    3,    2,  2,  10,   3,  5]  #Número mínimo de QSLs necesarias para obtener diploma platino
        self.ponderaciones = [0, 0.2, 0.5, 0.8, 1] #Número de QSLs necesarias para obtener diplomas inicial, bronce, plata, oro y platino (ponderacion de self.QSLsPlat)


    def actualizaDiplomas(self, indicativo, log):
        
        nQSLs = zeros(len(self.QSLsPlat))

        for qsl in log:
            if qsl["BAND"] == "160M" or qsl["BAND"] == "80M" or qsl["BAND"] == "40M" or qsl["BAND"] == "30M" or qsl["BAND"] == "20M" or qsl["BAND"] == "17M" or qsl["BAND"] == "15M" or qsl["BAND"] == "12M" or qsl["BAND"] == "10M":
                nQSLs[0]+=1
            elif "PROP_MODE" in qsl:
                if qsl["PROP_MODE"] == "SAT":
                    nQSLs[7]+=1
                elif qsl["PROP_MODE"] == "MS":
                    nQSLs[9]+=1
                elif qsl["PROP_MODE"] == "EME":
                    nQSLs[8]+=1
            elif qsl["BAND"] == "6M":
                nQSLs[1]+=1
            elif qsl["BAND"] == "4M":
                nQSLs[2]+=1
            elif qsl["BAND"] == "2M":
                nQSLs[3]+=1
            elif qsl["BAND"] == "70CM":
                nQSLs[4]+=1
            elif qsl["BAND"] == "23CM":
                nQSLs[5]+=1
            elif qsl["BAND"] == "13CM" or qsl["BAND"] == "9CM" or qsl["BAND"] == "6CM" or qsl["BAND"] == "3CM" or qsl["BAND"] == "1.25MM" or qsl["BAND"] == "6MM" or qsl["BAND"] == "4MM" or qsl["BAND"] == "2.5MM" or qsl["BAND"] == "2MM" or qsl["BAND"] == "1MM":
                nQSLs[4]+=1
            else:
                print("ERROR - Banda o propagación incorrecta")
                return

        
        arrayDiplomas = zeros([len(self.QSLsPlat), len(self.ponderaciones)+1], dtype=bool)

        for i in range(len(self.QSLsPlat)):
            for j in range(len(self.ponderaciones)):
                if j == 0:
                    if nQSLs[i]>0:
                        arrayDiplomas[i][j] = True
                else:
                    if nQSLs[i]>self.ponderaciones[j]*self.QSLsPlat[i]:
                        arrayDiplomas[i][j] = True
        return(arrayDiplomas)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, required=True, help="Indicativo de usuario")

    args = parser.parse_args()

    miAPI = APIFran()
    log = miAPI.getHistoricoQSLs(args.i)

    act = actualizador()
    updatedDip = act.actualizaDiplomas(args.i, log)

    miAPI.postNuevosDiplomas(args.i, updatedDip)


    

if __name__ == "__main__":
    main()
