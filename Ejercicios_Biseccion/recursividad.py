from math import cos, sin
from numbers import Number
from typing import Callable

"""
1. Implementar en Python el proceso anterior, que use una función (externa implementada, o bien pasada como parámetro),
 que lea el x como parámetro y un n natural, y luego sobre el ex inicial aplique la f n veces, f
 inalmente devolviendo el resultado obtenido tras la última aplicación.
 """


def recursive_result(arg: Number, reps: int, func: Callable) -> Number:
    for i in range(reps):
        result = func(arg)
        arg = result
    return result


"""
2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones, una f y una g, y que la aplicación
iterada sea una vez f, luego g, luego f, luego g, y así siguiendo, alternando una con otra, en total las veces que se especifique 
por el parámetro n, y finalmente devuelva el resultado obtenido tras la última aplicación.
"""


def composite_recursive_result(
    arg: Number, reps: int, func_a: Callable, func_b: Callable
) -> Number:
    for i in range(reps):
        result = func_a(arg)
        result = func_b(result)
        arg = result
    return result


if __name__ == "__main__":

    print(recursive_result(5, 100, cos))
    print(composite_recursive_result(5, 100, cos, sin))

    print(recursive_result(5, 10000, cos))
    print(composite_recursive_result(5, 10000, cos, sin))
    # terminan convergiendo
