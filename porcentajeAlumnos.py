#Un maestro desea saber que porcentaje de hombres y mujeres hay en un grupo de alumnos
#Solucion 1
print("Ingresa el numero de hombres")
Hombres = int(input())

print("Ingresa el numero de Mujeres")
Mujeres = int(input())

totalEstudiantes = Hombres + Mujeres
porcentajeHombres = (Hombres*100)/totalEstudiantes
porcentajeMujeres = (Mujeres*100)/totalEstudiantes

print("Porcentaje total de Hombres: ",porcentajeHombres,"%")
print("Porcentaje total de Mujeres: ",porcentajeMujeres,"%")

#Solucion 2
def porcentaje_alumnos(hombres,mujeres):
    totalEstudiantes = hombres + mujeres
    porcentajeHombres = (hombres*100)/totalEstudiantes
    porcentajeMujeres = (mujeres*100)/totalEstudiantes

    print("Porcentaje total de Hombres: ",porcentajeHombres,"%")
    print("Porcentaje total de Mujeres: ",porcentajeMujeres,"%")

porcentaje_alumnos(25,25)