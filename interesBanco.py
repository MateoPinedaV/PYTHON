#Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto dinero
#ganara despues de un mes si el banco paga a razon de 2% mensual

def interes_banco(dineroinvertido):
    interes = 0.02
    total = (dineroinvertido * interes)
    print("La ganacia pasado un mes es de: " + str (total))

interes_banco(200000)