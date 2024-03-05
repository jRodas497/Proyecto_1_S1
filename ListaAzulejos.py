from NodoAzulejo import NodoAzulejo

class ListaAzulejos:
    def __init__(self):
        self.first = None
        self.last = None
        
    def vacia(self):
        if self.first == None:
            return True
    
    def agregar_final(self, data):
        nuevoNodo = NodoAzulejo(data)
        if self.vacia():
            self.first = nuevoNodo
        else:
            local = self.first
            while local.next:
                local = local.next
            local.next = nuevoNodo
        
    def buscarPiso(self, codigo):
        local = self.first
        while local: 
            if local.data.nombre == codigo:
                return local.data
            local = local.next
        return None
    
    def buscarPatron(self, codigo):
        local = self.first
        while local: 
            if local.data.codigo == codigo:
                return local.data
            local = local.next
        return None
    
    def getNodo(self, id):
        count = 0
        local = self.first
        while local:
            if count == id:
                return local
            count += 1
            local = local.next
        return None
    
    def getValor(self, r, c):
        nodoR = self.getNodo(r)
        if nodoR:
            nodoC = nodoR.data.getNodo(c)
            if nodoC:
                return nodoC.data
        return None
    
    def flip(self, r, c):
        nodoR = self.getNodo(r)
        if nodoR:
            nodoC = nodoR.data.getNodo(c)
            if nodoC:
                nodoC.data = 'N' if nodoC.data == 'B' else 'B'
                
    def updateValor(self, r, c, value):
        nodoR = self.getNodo(r)
        if nodoR:
            nodoC = nodoR.data.getNodo(c)
            if nodoC:
                nodoC.data = value