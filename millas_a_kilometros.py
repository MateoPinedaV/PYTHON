def convertir_distancia(millas):
    km = millas *1.6
    return km                                       #convierte millas a kilometros

millas_recorrida = 55
recorrido_en_km = convertir_distancia(millas_recorrida)
print("La distancia en kilometros es: " + str (recorrido_en_km))
print("Ida y vuelta en kilometros es: " + str (recorrido_en_km*2))
