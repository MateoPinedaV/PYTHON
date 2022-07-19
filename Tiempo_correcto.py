#Dada una medida de tiempo xperesada en horas, minutos y segundos con valores arbitrarios, 
# elabore un programa que trasnforme dicha medida en una expresion
#correcta por ejemplo dada la medida 3h 118m 195s el programa debera dar como resultado 5h 1m 15s

from math import trunc


print("Ingrese el tiempo a convertir en expresion correcta (Horas,Minutos,Segundos)")

horas = float(input())
minutos = float(input())
segundos = float(input())

#Horas
HorasTotales = horas  +(minutos/60) + (segundos/3600)
HorasFinales = trunc(HorasTotales)

#Minutos
MinutosTotales = (HorasTotales-HorasFinales)*60
MinutosFinales = trunc(MinutosTotales)

#Segundos
SegundosFinales = (MinutosTotales-MinutosFinales)*60

print("La conversion de tiempo correcta es:",HorasFinales,"Horas --",MinutosFinales,"Minutos --",SegundosFinales,"Segundos --")
