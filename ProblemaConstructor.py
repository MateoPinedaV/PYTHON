#Un constructor sabe que necesita 0.5 metros cubicos de arena por metro cuadrado de revoque a realizar. 
# hacer un programa donde ingrese las medidas de una pared Largo y alto 
# expresada en metros y obtenga la cantidad de arena necesaria para revocarla

print("Ingrese el Alto en Metros")
alto = float(input())

print("Ingrese el Largo en Metros")
Largo = float(input())

area = (Largo*alto)
arena = (area*0.5)

print("El area de la pared es de:",area,"Metros")
print("La cantidad de arena necesaria es de:",arena,"Metros cubicos")