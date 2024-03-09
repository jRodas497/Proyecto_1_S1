from NodoAzulejo import NodoAzulejo
from ListaAzulejos import ListaAzulejos
class Patron:
    def __init__(self, codigo, patron):
        self.codigo = codigo
        self.patron = patron
        
    def __str__(self):
        return f'Patron: {self.patron}'