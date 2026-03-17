import sympy
from utils import div

# El método de newton se basa en aproximar la raíz a partir de las rectas tangentes a ciertos puntos de f
# La convergencia a una raíz no está garantizada pero si es C^2 y estamos en el entorno de  la raíz r
# Se puede asegurar que existe un e > 0 para el que si tomamos cualquier x0 del intervalo (r-e, r+3)
# Nos encontraremos con una sucesión que converge a r en xn


x = sympy.Symbol("x")
func = x**2 - 2


def metodo_newton(f, x0, error):
    if f.subs(x, x0) == 0:
        return x0
    dx_f = sympy.diff(f)
    try:
        x1 = x0 - div(f.subs(x, x0), dx_f.subs(x, x0))
        while abs(x1 - x0) > error:
            x0 = x1
            x1 = x0 - div(f.subs(x, x0), dx_f.subs(x, x0))
        return float(x1)
    except ZeroDivisionError:
        print(f"Error: f'(x) da 0 con x0 = {x0}")
        return x0


if __name__ == "__main__":
    print(metodo_newton(func, 1, 0.001))
    print(metodo_newton(func, 0, 0.001))

    # Solo funciona si estamos "cerca" pero parece que anda igual pero tarda
    # print(metodo_newton(func, 10000, 0.001))

    # 4 - Indicar cómo se puede usar el método de Newton para calcular la función
    # f(x) = ln x para x > 0, usando otras operaciones: +. -, *, / y exponencial. Discutir una posible
    # implementación práctica de esto

    func = sympy.log(x)

    # En este caso sí se nota que si no estamos cerca no termina nunca
    # Este esta cerca
    print(metodo_newton(func, 2, 0.0001))

    # Este no
    # print(metodo_newton(func,5, 0.0001))
