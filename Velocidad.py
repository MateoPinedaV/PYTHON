#Mostrar la velocidad inicial sin conocerla

from math import sqrt

if __name__ == '__main__':
	
	vi = float()
	vf = float()
	a = float()
	d = float()
	
	print("ingrese la velocidad final en m/s")
	
	vf = float(input())
	
	print("ingrese la aceleracion en metros sobre m/s^2")
	
	a = float(input())
	
	print("ingrese la distancia recorrida en mts")
	
	d = float(input())
	
	if vf**2-2*a*d>=0:
		vi = sqrt(vf**2-2*a*d)
		print("la velocidad inicial es ",vi,"m/s")
	else:
		print("No tiene solucion en los reales")

