import xml.etree.cElementTree as ET
from Piso import Piso
from Patron import Patron
import os
import funciones as f

def main():
    print("------------------------------------------------------")
    print("*** PROYECTO 1 -- INTRODUCCIÓN A LA PROGRAMACIÓN 2 ***")
    print("------------------------------------------------------")
    menu()

def menu():
    print("")
    print("-------------------------------------------------------")
    print("#############   LECTURA DE ARCHIVOS XML   #############")
    print("#############   PISOS DE GUATEMALA, S.A.  #############")
    print("-------------------------------------------------------")

    print("-------------------------------------------------------")
    print("| 1. CARGAR ARCHIVO                                   |")
    print("| 2. ESCRIBIR ARCHIVO SALIDA                          |")
    print("| 2. MANEJO DE PATRONES                               |")
    print("| 4. DATOS DEL ESTUDIANTE                             |")
    print("| 5. GENERAR GRÁFICA                                  |")
    print("| 6. INICIALIZAR SISTEMA                              |")
    print("| 7. SALIR                                            |")
    print("-------------------------------------------------------")
    
    print("")
    print("## INGRESE UNA OPCION: ##")
    opcion = input()
    print("")
    
    if opcion == "1":
        try:
            if os.path.exists('pisos.xml') == False:
                print('** ARCHIVO NO ENCONTRADO **')
            else:
                print(arch)
                print("\n## ARCHIVO CARGADO CON EXITO ##")
        except:
            print("** ERROR **")
        menu()
    elif opcion == '2':        
        menu()
    elif opcion == '2':
        print('')
    elif opcion == '2':
        print('')
    elif opcion == '2':
        print('')
    elif opcion == '2':
        print('')
    elif opcion == '7':
        print('++Adios, nos vemos!++')
    else:
        print('++Opción no valida :(++')
        menu()
    
def datos_estudiante():
    print("------------------------------------------------")
    print("############# DATOS DEL ESTUDIANTE #############")
    print("------------------------------------------------")
    print("-> JUAN JOSÉ RODAS MANSILLA ")
    print("-> 202200389 ")
    print("-> Introducción a la Programación y Computación 2 sección 'A' ")
    print("-> Ingenieria en Ciencias y Sistemas ")
main()