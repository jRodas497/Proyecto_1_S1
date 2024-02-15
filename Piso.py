class Piso:
    def __init__(self, nombre, rows, colums, flip, switch, patrones):
        self.nombre = nombre
        self.rows = rows
        self.colums = colums
        self.flip = flip
        self.switch = switch
        self.patrones = patrones
        
    def __str__(self):  
        return f'Nombre: {self.nombre}, Filas: {self.rows}, Columnas: {self.colums}, Voltear: {self.flip}, Intercambiar: {self.switch}'
    