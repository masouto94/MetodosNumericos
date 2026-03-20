from Ejercicios_Biseccion.biseccion import triseccion
from Ejercicios_Newton.metodo_newton import metodo_newton
from math import log
from utils import SYMBOLS


def funcion_grande():
    x = SYMBOLS.get("x")
    return x**6 + 5 * x**5 - 4 * x**4 - 3 * x**3 - 2 * x**2 - 5 * x + 10


def combinado(a, b, func, error, max_steps):
    x0 = triseccion(a, b, func, error, max_steps)
    return metodo_newton(func, x0, error * 10e-6)


if __name__ == "__main__":

    a = -1000
    b = -5
    print(
        f"Raiz aproximada para intervalo [{a},{b}]",
        combinado(a, b, funcion_grande, 0.01, log(abs(a - b), 2)),
    )
    a = -5
    b = 1000
    print(
        f"Raiz aproximada para intervalo [{a},{b}]",
        combinado(a, b, funcion_grande, 0.01, log(abs(a - b), 2)),
    )
