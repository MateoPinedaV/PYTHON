#Calcular el numero de pulsacopnes que una persona debe tener por cada 10 segundos de ejercicio
#si la fomrula es numpulsaciones = (220-edad)/10

#Solucion 1
print("Ingrese su edad")
edad = int(input())
pulsaciones = (220-edad)/10

print("El numero de pulsaciones que debes tener por cada 10 segundos es",pulsaciones)

#Solucion 2
def numero_pulsaciones(Edad):
    pulsaciones = (220-Edad)/10
    print("El numero de pulsaciones que debes tener por cada 10 segundos es",pulsaciones)

numero_pulsaciones(17)
