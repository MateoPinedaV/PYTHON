#Escribir un programa al cual ingrese la velocidad de un movil expresada en metros 
#por segundo e imprima en pantalla la velocidad en kilometros por hora

def  metrosAkilometros (metrosSeg):
    conversion = (metrosSeg/1000) * 3600
    print("La velocidad en kilometros por hora es: ",conversion)


metrosAkilometros(10)
