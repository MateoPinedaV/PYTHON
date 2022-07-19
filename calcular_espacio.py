def calcular_espacio(archivos):
    tamaño_archivo = 4096
    tamañaño_completo = archivos/tamaño_archivo
    parte_tamaño = archivos % tamaño_archivo

    if parte_tamaño > 0:
        return tamañaño_completo * tamaño_archivo + tamaño_archivo
    return tamañaño_completo * tamaño_archivo

print(calcular_espacio(1))
print(calcular_espacio(4096))
print(calcular_espacio(4097))
