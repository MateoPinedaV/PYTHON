def convertir_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos - horas * 3600) // 60
    resta_segundos=segundos - horas * 3600 - minutos * 60
    return horas,minutos,resta_segundos

convertir_segundos(20)