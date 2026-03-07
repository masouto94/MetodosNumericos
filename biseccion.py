from math import inf
from numbers import Number
from typing import Callable
from math import cos, pi
import logging

logger = logging.getLogger()
# Cambiar INFO por DEBUG para que muestre todos los pasos intermedios
logging.basicConfig(level="INFO", format="%(levelname)s - %(funcName)s - %(message)s")


def signo(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1


"""
8. Modificar la implementación del método de bisección para que:

a) haga la menor cantidad posible de evaluaciones de la f en cada iteración

b) vaya imprimiendo la secuencia de los puntos p que van aproximando a la raíz buscada

c) que tenga una cota (grande) en la cantidad total de pasos que dará antes de devolver algo

d) que devuelva, además del p encontrado, la cantidad de pasos que fueron necesarios para llegar a la aproximación buscad

"""


def biseccion(a: Number, b: Number, func: Callable, error=0.5, max_steps: int = inf):
    c = (a + b) / 2
    if signo(func(a)) * signo(func(b)) >= 0:
        logger.warning(
            f"El intervalo [{a},{b}] no contiene una raíz porque no hay cambio de signo"
        )
        return None
    step = 0
    while (b - a) > error and step < max_steps:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        if signo(func(a)) * signo(func(c)) < 0:
            b = c
        else:
            a = c
        step += 1
        logger.debug(f"punto:{c}")
    logger.debug(f"Pasos necesarios:{step}")
    return c


"""4. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 5, 
comenzando con el intervalo [1,2], y el error epsilon = 0.5.
"""
a = 1
b = 2


def f1(x):
    return x**3 + x - 5


print(biseccion(a, b, f1))

"""5. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 10 
haciendo 4 pasos.
"""


def f2(x):
    return x**3 + x - 10


a = 1
b = 10
print(biseccion(a, b, f2, max_steps=4))
# Exacto es 2

"""6. Aplicar el método de bisección para hallar una aproximación de un x que cumpla x^2 + x = 12. 
Calcular luego el valor exacto de otra manera, y comparar.
"""

a = 1
b = 12


def f3(x):
    return x**2 + x - 12


print(biseccion(a, b, f3, error=1 / 10))
# Exacto es 3

"""7. Aplicar el método de bisección para aproximar un x que cumpla cos(x) = -1, con error menor que epsilon = 1/10.
 Notar que esto sirve para encontrar aproximaciones de pi.
"""


def f4(x):
    return cos(x) + 1


a = 0
b = 5
print(biseccion(a, b, f4, error=1 / 10))
# No se puede calcular con este algoritmo porque la expresion cos(x) + 1 nunca es negativa. No cumple el cambio de signo
# porque esa función tiene conjunto imagen [0,2]

"""9. Método de trisección. Implementar en Python un método para aproximar raíces al estilo de bisección, 
pero que en vez de dividir el intervalo en 2 subintervalos lo divida en 3, y en cada iteración elija uno 
de los 3 subintervalos que contenga una raíz. Usar una condición de parada análoga a la del método de bisección."""


def triseccion(a: Number, b: Number, func: Callable, error=0.5, max_steps: int = inf):
    c1 = a + (b - a) / 3
    c2 = b - (b - a) / 3
    if signo(func(a)) == signo(func(b)) == signo(func(c1)) == signo(func(c2)):
        logger.warning(
            f"El intervalo [{a},{b}] no contiene una raíz porque no hay cambio de signo"
        )
        return None
    step = 0
    while (b - a) > error and step < max_steps:
        c1 = a + (b - a) / 3
        c2 = b - (b - a) / 3
        if func(c1) == 0:
            return c1
        if func(c2) == 0:
            return c2
        if signo(func(a)) * signo(func(c1)) < 0:
            b = c1
        elif signo(func(a)) * signo(func(c2)) < 0:
            b = c2
        else:
            a = c2
        step += 1
    return (c1 + c2) / 2


a = 1
b = 12


def f3(x):
    return x**2 + x - 12


print(triseccion(a, b, f3, error=1 / 10))
