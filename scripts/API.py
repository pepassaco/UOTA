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
        #le mando a la api un array de QSLs (en formato de diccionarios) de los nuevos contactos
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