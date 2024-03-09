from NodoAzulejo import NodoAzulejo

class Piso:
    def __init__(self, nombre, r, c, f, s):
        self.nombre = nombre
        self.r = r
        self.c = c
        self.f = f
        self.s = s
        self.patrones = []
        self.row = None
        
    def __str__(self):  
        return f'Nombre: {self.nombre}, Filas: {self.rows}, Columnas: {self.colums}, Voltear: {self.flip}, Intercambiar: {self.switch}'
    
    
    def agregarPatron(self, codigo):
        fila = self.row
        while fila:
            actual = fila
            while actual:
                print(actual.color, end = '')
                actual = actual.derecha
            actual = actual.abajo
        
    def cadena(self, row, codigo):
        row.codigo = codigo
        if not self.row:
            self.row = row
        else:
            last = self.row
            while last.bot:
                last = last.bot
            last.bot =row
        
        self.patrones[codigo] = row
        self.patrones = dict(sorted(self.patrones.items()))