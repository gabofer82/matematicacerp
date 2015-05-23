# -*- coding: utf-8 -*-


########################################################
#                     OPERACIONES                      #
########################################################
def linealDosPorDos(datos):
    formato_correcto, datos = parserDosPorDos(datos)
    if formato_correcto:
        return 'Lineal Dos por Dos'
    else:
        return -1


def linealTresPorTres(datos):
    formato_correcto, datos = parserTresPorTres(datos)
    if formato_correcto:
        return 'Lineal Tres por Tres'
    else:
        return -1


def sumaMatrices(datos):
    formato_correcto, datos = parserSumaMatrices(datos)
    if formato_correcto:
        return 'Suma Matrices'
    else:
        return -1


def productoDeMatrices(datos):
    formato_correcto, datos = parserProductoMatrices(datos)
    if formato_correcto:
        return 'Producto Matrices'
    else:
        return -1
    

########################################################
#                       PARSERS                        #
########################################################
def parserDosPorDos(datos):
    return None, None


def parserDatosTresPorTres(datos):
    return None, None


def parserSumaMatrices(datos):
    return None


def parserProductoMatrices(datos):
    return None, None

