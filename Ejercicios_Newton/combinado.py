from Ejercicios_Biseccion.biseccion import triseccion
from Ejercicios_Newton.metodo_newton import metodo_newton
import sympy
from utils import div

x = sympy.Symbol("x")

funcion_grande = x**6 + 5 * x**5 - 4 * x**4 - 3 * x**3 - 2 * x**2 - 5 * x + 10


def combinado(a, b, func, error, max_steps):
    x0 = triseccion(a, b, func, error, max_steps)
    return metodo_newton(func, x0, error * 10e-6)


# Falta cambiar la implementacion de las funcs en biseccion para que tomen la func definida con sympy
if __name__ == "__main__":

    print(combinado(-1000, 1000, funcion_grande, 0.01, 100))
