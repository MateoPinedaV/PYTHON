def imprimir_factor_primo(numero):
    factor=2
    while factor <= numero:
        if numero % factor == 0:             #Factor primo de un numero
            print(factor)
            numero=numero/factor
        else:
            factor+=1
    return "Terminado"

imprimir_factor_primo(100)