import xml.etree.cElementTree as ET
from Piso import Piso
from Patron import Patron
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import funciones as f
from ListaAzulejos import ListaAzulejos

def main():
    print("------------------------------------------------------")
    print("*** PROYECTO 1 -- INTRODUCCIÓN A LA PROGRAMACIÓN 2 ***")
    print("------------------------------------------------------")
    menu()

def loadXML(docx):
    pisos = ListaAzulejos()
    tree = ET.parse(docx)
    root = tree.getroot()
    for xml in root.findall('pisos'):
        nombre = xml.attrib['nombre']
        R = int(xml.find('R').text)
        C = int(xml.find('R').text)
        F = int(xml.find('R').text)
        S = int(xml.nombre, R, C, F, S)
        piso = Piso(nombre, R, C, F, S)


def menu():
    print("")
    print("-------------------------------------------------------")
    print("#############   LECTURA DE ARCHIVOS XML   #############")
    print("#############   PISOS DE GUATEMALA, S.A.  #############")
    print("-------------------------------------------------------")

    print("-------------------------------------------------------")
    print("| 1. SALIR                                            |")
    print("| 2. LISTADO DE PATRONES                              |")
    print("| 2. ESCOGER LISTADO                                  |")
    print("| 4. DATOS DEL ESTUDIANTE                             |")    
    print("-------------------------------------------------------")
    
    print("")
    print("## INGRESE UNA OPCION: ##")
    opcion = input()
    print("")
    
    if opcion == "1":
        print('++Adios, nos vemos!++')
    elif opcion == '2':        
        f.reportePiPa()
        menu()
    elif opcion == '3':
        nombre = input('Nombre del piso: ')
        co = input('Código inicial: ')
        cd = input('Código final: ')
        pasos = f.cambiar(nombre, co, cd)
        
        guardar = input('Las instrucciones se guardaran en un PDF. Desea continuar? (S/N): ').upper()
        if guardar == 'S':
            pdf(pasos)
            
        else:
            print('Instrucciones:')
            for p in pasos:
                print(p)
        menu()
        
    elif opcion == '4':
        datos_estudiante()
    else:
        print('++Opción no valida :(++')
        menu()
    
def pdf(pasos):
    c = canvas.Canvas('Pasos.pdf', pagesize=letter)
    h = 700
    for p in pasos:
        c.drawString(100, h, p)
        y -= 20
    c.save
    print('Se ha generado el PDF para los pasos')
    menu()
    
def datos_estudiante():
    print("------------------------------------------------")
    print("############# DATOS DEL ESTUDIANTE #############")
    print("------------------------------------------------")
    print("-> JUAN JOSÉ RODAS MANSILLA ")
    print("-> 202200389 ")
    print("-> Introducción a la Programación y Computación 2 sección 'A' ")
    print("-> Ingenieria en Ciencias y Sistemas ")
    
    menu()
    
if __name__ == "__main__":
    main()