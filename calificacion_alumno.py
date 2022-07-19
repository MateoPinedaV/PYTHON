# un alumno desea saber cual sera su promedio general en las tres mataerias mas dificiles que cursa y cual sera el
# promedio que obtendra en cada una de ellas estas materias se evalucan como se muestra a continuacion:
# Matematicas examen 90% tareas 10%  (3 tareas)
# Fisica exmanen 80% tareas 20%  (2 tareas)
# Quimica examen 85% tareas 15%  (3 tareas)

print("Ingrese la calificacion del examen de matematicas")
calificacionExamen = float(input())

print("Ingrese las calificaciones de las 3 tareas")
a = float(input())
b = float(input())
c = float(input())
tareas = (a+b+c)/3
Promedio1 = (calificacionExamen * 0.90) + (tareas * 0.10) 

print("Ingrese la calificacion del examen de Fisica")
calificacionExamen = float(input())

print("Ingrese las calificaciones de las 2 tareas")
a = float(input())
b = float(input())
tareas = (a+b)/2
Promedio2 = (calificacionExamen * 0.80) + (tareas * 0.20)

print("Ingrese la calificacion del examen de Quimica")
calificacionExamen = float(input())

print("Ingrese las calificaciones de las 3 tareas")
a = float(input())
b = float(input())
c = float(input())
tareas = (a+b+c)/3
Promedio3 = (calificacionExamen * 0.85) + (tareas * 0.15)

promedioGeneral = (Promedio1+Promedio2+Promedio3)/3

print("El promedio de Matematicas es:",Promedio1)
print("El promedio de Fisica es",Promedio2)
print("El promedio de Quimica es:",Promedio3)
print("El promedio general de todas las materias es:",promedioGeneral)



