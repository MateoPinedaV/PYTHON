#En un hospital existen 3 areas: ginecologia, pediatria, traumatologia. el presupuesto anual del hospital se reparte
#conforme a la siguiente tabla
#ginecologia 40%
#traumatologia 30%
#pediatria 30%
#obtener la cantidad de dinero que recibira cada area para cualquier monto presupuestal

def monto_presupuestal(Dinero):
    print("Al area de ginecologia le corresponde: $",Dinero* 0.40)
    print("Al area de pediatria le corresponde: $",Dinero * 0.30)
    print("Al area de traumatologia  le corresponde: $",Dinero * 0.30)


monto_presupuestal(100000)