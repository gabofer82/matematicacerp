# -*- coding: utf-8 -*-
import os

#GLOBALES
AUTORES = 'Autores: Gabriel Fernández' 


def mostrarMenuPrincipal():
    os.system('clear')
    print 'BIENVENIDO A CALCULADORA 2015!'
    print AUTORES
    print 'Digite su opción y presione enter:'
    print '1. Sistemas lineales de 2x2'
    print '2. Sistemas lineales de 3x3'
    print '3. Suma de matrices'
    print '4. Producto de matrices'
    print '0. Salir.'
    res = raw_input('Opción: ')
    if res == '':
        return -1
    else:
        return int(res)
    
def mostrarOpcionUno():
    os.system('clear')
    print 'Sistema lineal de 2x2'
    print AUTORES
    print 'Ingrese a1: (y así sucesivamente b1 y c1, luego a2, b2 y c2)'
    print 'Luego mostrará la solución x = x1 e y = y1'
    print 'Presione enter para volver al menú principal.'
    
    vueltas = 0
    datos = []
    while vueltas > 0:
        entrada = raw_input('Datos: ')
        if len(entrada) > 0:
            datos[1] = entrada
        else:
            return entrada
    
    return datos
    
    
def mostrarOpcionDos():
    # Para facilitar la tarea en este caso sólo resolverá sistemas que sean
    # compatibles determinados.
    os.system('clear')
    print 'Opción 2:'
    print 'Sistema lineal de 3x3'
    print AUTORES
    print 'Ingrese a1: (y así sucesivamente b1 , c1 y d1 ,etc)'
    print 'Luego mostrará la solución x = x1 ; y = y1 z = z1'
    print 'Presione enter para volver al menú principal.'
    
    rango = 3
    datos = []
    for i in range(rango):
        datos[i] = raw_input('Datos: ')
    
    return datos
    
    
def mostrarOpcionTres():
    os.system('clear')
    print 'Suma de Matrices'
    print AUTORES
    print 'Ingrese las dimensiones de las matrices separadas por “,”. Ejemplo 2,3'
    print '(recordar que las matrices deben tener la misma dimensión por lo que se'
    print 'pide una sola vez la dimensión).'
    print 'El sistema solicita el ingreso de los elementos de la primera matriz.'
    print 'Ingrese a11, a12, a13, a21, a22, a23.'
    print 'Ingrese b11, b12, b13, b21, b22, b23.'
    print 'Luego realiza el producto y muestra las matrices y el resultado.'
    print 'Presione enter para volver al menú principal.'
    return raw_input('Datos: ')
    
    
def mostrarOpcionCuatro():
    os.system('clear')
    print 'Producto de Matrices'
    print AUTORES
    print 'Ingrese las dimensiones de la primera matriz separadas por “,”'
    print 'Ejemplo 2,3'
    print 'Ingrese las dimensiones de la segunda matriz separadas por “,”'
    print 'Ejemplo 3,5.'
    print 'Presione enter para volver al menú principal.'
    return raw_input('Datos: ')
    