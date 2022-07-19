equipos = [ 'ATL NACIONAL' , 'DEP CALI' , 'SANTA FE' , 'JUNIOR' ]
for equipo_local in equipos:
    for equipo_visitante in equipos:
        if equipo_local!=  equipo_visitante:
            print(equipo_local + " vs " + equipo_visitante)

#Emparejamiento aleatorio de equipos sin que se repitan