#2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones, 
#una f y una g, y que la aplicación iterada sea una vez f, luego g, luego f, luego g, y así 
#siguiendo, alternando una con otra, en total las veces que se especifique por el parámetro 
#n, y finalmente devuelva el resultado obtenido tras la última aplicación. 

from math import *

def f(x):
    return x+1
    
def g(x):
    return x-1

def mi_funcion_recursiva(x, n):
    if n == 0:
        return x
    if n%2 == 0:
        x = f(x)
    elif n%2 == 1:
        x = g(x)
    print(x)
    mi_funcion_recursiva(x, n-1)


mi_funcion_recursiva(1, 10)