#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto
#debera pagar finalemente por su compra

print("Ingrese el valor de su compra")
valorCompra = float (input())
descuento = 0.15
AplicarDescuento = (valorCompra * descuento)
total = valorCompra - AplicarDescuento

print("El valor final de su compra es:",total,"Pesos")

