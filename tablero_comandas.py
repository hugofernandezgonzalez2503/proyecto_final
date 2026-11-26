class TableroComandas:
    def __init__(self, ancho, alto):
        self.ancho=ancho
        self.alto=alto
        self.comandas = []
    
    def agregar_comanda(self, comanda):
        self.comandas.append(comanda)

    def eliminar_comanda(self, comanda):
        if comanda in self.comandas:
            self.comandas.remove(comanda)

    def mostrar_comandas(self):
        for comanda in self.comandas:
            print(comanda)