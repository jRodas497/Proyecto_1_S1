import os
from Patron import Patron
from Piso import Piso
import xml.etree.cElementTree as ET

listaPatrones = []

def leerArchivoET():

    file_path = os.path.join(os.path.dirname(__file__), 'pisos.xml')
    tree = ET.parse(file_path) #Parsear el archivo XML
    root = tree.getroot()

    for element in root.findall('piso'):
        nombrePiso = element.get('nombre')
        filas = element.find().text
        columnas = element.find().text
        flip = element.find().text
        switch = element.find().text

        piso = Piso(nombrePiso, filas, columnas, flip, switch, [])

        for codigoElement in element.find('patrones').findall('patron'):
            codigoE = codigoElement.get('codigo')
            patronE = codigoElement.find('patron').text
            
            patron = Patron(codigoE, patronE)
            piso.patrones.append(patron)
            
        listaPatrones.append(piso)