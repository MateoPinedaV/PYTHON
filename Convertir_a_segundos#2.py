#version 2

def convertir_segundos(horas, minutos , segundos):
    return 3600*horas + 60*minutos + segundos

tiempo_a=convertir_segundos(2,30,0)  #En caso de que no se conozca algun valor poner 0
tiempo_b=convertir_segundos(0,45,15)
resultado= tiempo_a+tiempo_b
print(resultado)