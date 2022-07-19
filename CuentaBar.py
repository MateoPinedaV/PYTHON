from typing_extensions import Self

#Programa cuenta Bar
class cuenta:

    menu = {
        'vino':4000,
        'cerveza':3000,
        'refresco':2000,
        'pollo':10000,
        'carne':15000,
        'ensalada':12000,
        'postre':6000

    }

    def __init__(self):
        self.total = 0
        self.objetos = []

    def add(self,objeto):
        self.objetos.append(objeto)
        self.total += self.menu[objeto]
    
    def imprimir_factura(self,impuesto,servicio):
        impuesto = (impuesto/100)*self.total
        servicio = (servicio/100)*self.total
        total = self.total + impuesto + servicio

        for objeto in self.objetos:
            print(f'{objeto:20} ${self.menu[objeto]}')

        print(f'{"Total":20} ${total:.2f}')

    

        