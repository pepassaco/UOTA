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
from API import APIFran


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
