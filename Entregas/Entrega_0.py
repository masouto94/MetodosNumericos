from Ejercicios_Biseccion.biseccion import triseccion
from Ejercicios_Newton.metodo_newton import metodo_newton
from math import log, inf
from numbers import Number
import logging
import sympy


SYMBOLS = {
    symbol: sympy.Symbol(symbol) for symbol in list("abcdefghijklmnopqrstuvwxyz")
}
logger = logging.getLogger()
# Cambiar INFO por DEBUG para que muestre todos los pasos intermedios
logging.basicConfig(level="INFO", format="%(levelname)s - %(funcName)s - %(message)s")


# Fuerzo que al dividir por cero tire error
def div(num, den):
    if den.is_zero:
        raise ZeroDivisionError("División por cero")
    return num / den


def signo(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1


def triseccion(a: Number, b: Number, expr, error=0.5, max_steps: int = inf):
    func = expr()
    c1 = a + (b - a) / 3
    c2 = b - (b - a) / 3
    if (
        signo(func.subs(SYMBOLS.get("x"), a))
        == signo(func.subs(SYMBOLS.get("x"), b))
        == signo(func.subs(SYMBOLS.get("x"), c1))
        == signo(func.subs(SYMBOLS.get("x"), c2))
    ):
        logger.warning(
            f"El intervalo [{a},{b}] no contiene una raíz porque no hay cambio de signo"
        )
        return None
    step = 0
    while (b - a) > error and step < max_steps:
        c1 = a + (b - a) / 3
        c2 = b - (b - a) / 3
        if func.subs(SYMBOLS.get("x"), c1) == 0:
            return c1
        if func.subs(SYMBOLS.get("x"), c2) == 0:
            return c2
        if (
            signo(func.subs(SYMBOLS.get("x"), a))
            * signo(func.subs(SYMBOLS.get("x"), c1))
            < 0
        ):
            b = c1
        elif (
            signo(func.subs(SYMBOLS.get("x"), a))
            * signo(func.subs(SYMBOLS.get("x"), c2))
            < 0
        ):
            b = c2
        else:
            a = c2
        step += 1
    return (c1 + c2) / 2


def metodo_newton(expr, x0, error):
    f = expr()
    if f.subs(SYMBOLS.get("x"), x0) == 0:
        return x0
    dx_f = sympy.diff(f)
    try:
        x1 = x0 - div(f.subs(SYMBOLS.get("x"), x0), dx_f.subs(SYMBOLS.get("x"), x0))
        while abs(x1 - x0) > error:
            x0 = x1
            x1 = x0 - div(f.subs(SYMBOLS.get("x"), x0), dx_f.subs(SYMBOLS.get("x"), x0))
        return float(x1)
    except ZeroDivisionError:
        print(f"Error: f'(x) da 0 con x0 = {x0}")
        return x0


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
