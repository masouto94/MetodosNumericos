#1. Implementar en Python el proceso anterior, que use una función (externa 
#implementada, o bien pasada como parámetro), que lea el x como parámetro y un n 
#natural, y luego sobre el x inicial aplique la f n veces, finalmente devolviendo el resultado 
#obtenido tras la última aplicación.

from math import *

def mi_funcion(x0, n):
    if n == 0:
        return
    x1 = cos(x0)
    print(x1)
    mi_funcion(x1, n-1)


mi_funcion(1, 50)
