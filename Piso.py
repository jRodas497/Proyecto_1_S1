from ListaAzulejos import ListaAzulejos
from Patron import Patron

class Piso:
    def __init__(self, nombre, r, c, f, s, patrones):
        self.nombre = nombre
        self.r = r
        self.c = c
        self.f = f
        self.s = s
        self.patrones = patrones
        
    def __str__(self):  
        return f'Nombre: {self.nombre}, Filas: {self.rows}, Columnas: {self.colums}, Voltear: {self.flip}, Intercambiar: {self.switch}'
    