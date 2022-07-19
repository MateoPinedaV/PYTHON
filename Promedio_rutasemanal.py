#Todos los Lunes, Miercoles y viernes una persona corre la misma ruta y cronometra los tiempos obtenidos
#determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera

print("Ingrese la ruta recorrrida en KM")
ruta = int(input())

print("Ingrese el tiempo del dia Lunes")
tiempoLunes = float(input())

print("Ingrese el tiempo del dia Martes")
tiempoMiercoles = float(input())

print("Ingrese el tiempo del dia Viernes")
tiempoViernes = float(input())

promedio = (tiempoLunes+tiempoMiercoles+tiempoViernes)/3

print("El tiempo promedio que tarda en recorrer la ruta semanal de:",ruta,"KM","es de:",promedio,"Minutos")