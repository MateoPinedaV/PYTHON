#Escribir un programa que calcule el salario de un trabajador de la manera siguiente. el trabajador cobra un 
# precio fijo por hora y se le descuenta el 10% en concepto de impuesto de renta. el programa 
# debe pedir el nombre del trabajador, las horas trabajadas , y el precio que cobra por hora
#como salida debe imprimir el sueldo bruto, el descuento de renta y el salario a pagar

print("Ingresa Tu nombre")
nombre = str(input())

print("Ingresa las horas trabajadas")
horasTrabajadas = int(input())

print("Ingresa el precio que cobras por hora")
precioporHora = float(input())

SueloBruto = (horasTrabajadas*precioporHora)
DescuentoRenta = (SueloBruto*0.10)
TotalPagar = (SueloBruto - DescuentoRenta)

print(nombre,"Tu sueldo bruto es de: $",SueloBruto)
print("El descuento de renta es de: $",DescuentoRenta)
print("El salario total a pagar es de: $",TotalPagar)

	