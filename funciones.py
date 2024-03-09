import xml.etree.ElementTree as ET
from Piso import Piso
from NodoAzulejo import NodoAzulejo
from graphviz import Digraph
###
class PisosGuatemala:
    def __init__(self):
        self.pisos = {}
###
    def subirXML(self, ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for xml in root.findall('piso'):
            nombre = xml.attrib['nombre']
            R = int(xml.find('R').text)
            C = int(xml.find('C').text)
            F = int(xml.find('F').text)
            S = int(xml.find('S').text)
            piso = Piso(nombre, R, C, F, S)
            
            for patron in xml.find('patrones').findall('patron'):
                codigo = patron.attrib['codigo']
                patron = patron.text.strip()
                piso.cadena(self.fila(patron, C), codigo)
                
            self.pisos[nombre] = piso
###
    def fila(self, patron, C):
        primer = None
        ultimo = None
        for color in patron:
            azulejo = NodoAzulejo(color)
            if not primer:
                primer = azulejo
            else:
                ultimo.next = azulejo
            ultimo = azulejo
        return primer
###
    def reportePiPa(self):
        print("Pisos y patrones:")
        
        for nombre, piso in sorted(self.pisos.items()):
            print(f"Piso: {nombre}")
            piso.agregarPatron('')
###
    def ordenar(self):
        print("Listado en orden:")
        for nombre, piso in sorted(self.pisos.items()):
            print(f"Piso: {nombre}")
            for codigo, row in piso.patrones.items():
                print(f"Código de patrón: {codigo}")
                patron = ""
                local = row
                while local:
                    patron += local.data
                    local = local.next
                print(f"Patrón: {patron}")
                print()
###
    def cambiar(self, nombre, o, d):
        piso = self.pisos.get(nombre)
        if not piso:
            print("Piso no encontrado")
            return
        po = self.patronXML(piso, o)
        pd = self.patronXML(piso, d)
        print(f"Patrón anterior: {po}")
        print(f"Patrón actual:   {pd}")
        
        minimo, opcion = self.minimo(po, pd, piso.f, piso.s)
        
        print(f"El mínimo para este cambio es de: Q{minimo}")
        for i, opt in enumerate(opcion, start=1):
            print(f"{i}. {opt}")
        
        self.grafica(nombre, d)
        return opcion
###
    def patronXML(self, piso, cp):
        row = piso.patrones.get(cp)
        if row:
            local = row
            patron = ""
            while local:
                patron += local.data
                local = local.next
            return patron
        else:
            print("Código del patron no encontrado")
### 
    def minimo(self, po, pd, flipCost, switchCost):
       
        po = list(po)
        pd = list(pd)
        
        total = 0
        orden = []
        
        for i in range(len(po)):
            if po[i] != pd[i]:
                flipT = flipCost if po[i] != pd[i] else float('inf')
                switchT = switchCost if i < len(po) - 1 and po[i] != po[i + 1] else float('inf')
                
                if flipT < switchT:
                    total += flipT
                    orden.append(f"Voltear en {i + 1}")
                    po[i] = 'N' if po[i] == 'B' else 'B'
                else:
                    total += switchT
                    orden.append(f"Intercambiar en {i + 1}")
                    po[i], po[i + 1] = po[i + 1], po[i]
        
        return total, orden
###     
    def grafica(self, nombre, cp):
        piso = self.pisos.get(nombre)
        if not piso:
            print("El piso no se ha registrado")
            return

        patron = self.patronXML(piso, cp)
        if not patron:
            print("El código para el patron no existe")
            return

        dot = Digraph()
        dot.node_attr['shape'] = 'plaintext'
        dot.edge_attr['style'] = 'invis'
        label = f'##### Nombre = {nombre} ##### Código del Patrón = {cp} #####'
        dot.attr(label=label)

        tabla = f'<<TABLE border="1" cellspacing="0" cellpadding="10">'
        colores = {'N': 'black', 'B': 'white'}
        rows = piso.r
        columns = piso.c

        for i in range(rows):
            tabla += '<tr>'
            for j in range(columns):
                id = i * columns + j
                color = patron[id]
                bg = colores.get(color)
                tabla += f'<td bgcolor="{bg}"></td>'
            tabla += '</tr>'
        tabla += '</TABLE>>'
        dot.node('piso', label=tabla, shape='none')
        dot.render('patron', format='png', cleanup=True)
###