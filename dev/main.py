#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# Este software ha sido desarrollado por Gabriel Fernández                    #
# (gabofer82@gmail.com) con el único proposito de aprobar el obligatorio I de #
# la asignatura Matemática II de segundo año de profesorado de Informática    #
# dictado en CERP litoral, año 2015.                                          #
###############################################################################
# Imports
from menues import (mostrarMenuPrincipal, mostrarOpcionUno,
                   mostrarOpcionDos, mostrarOpcionTres,
                   mostrarOpcionCuatro)
from operaciones import (linealDosPorDos, linealTresPorTres,
                        sumaMatrices, productoDeMatrices)


def main():
    motor()


def motor():
    opcion = -1
    
    while opcion:  # motor principal de la aplicacion, marcha
        #  mientras opcion != 0
        opcion = mostrarMenuPrincipal()
        
        if opcion == 1:  # si usuario escoge 1
            datos = mostrarOpcionUno()
            if datos:
                opcion = linealDosPorDos(datos)
        elif opcion == 2: # si usuario escoge 2
            datos = mostrarOpcionDos()
            opcion = linealTresPorTres(datos)
        elif opcion == 3: # si usuario escoge 3
            datos = mostrarOpcionTres()
            opcion = sumarMatrices(datos)
        elif opcion == 4: # si usuario escoge 4
            datos = mostrarOpcionCuatro()
            opcion = productoDeMatrices(datos)
        elif opcion == 0:  # si el usuario escoge 0
            # finaliza la aplicacion
            opcion = 0
        else: # si usuario escoge cualquier otra cosa
            # no pasa nada y reinicia el ciclo
            opcion = -1
            
    return opcion
    


if __name__ == '__main__':
    salida = main()
    print salida
