import sympy as sp

x = sp.Symbol('x')

mi_funcion = x**3 + 1
derivada = sp.diff(mi_funcion, x)

error = 0.0001

def formula_newton(x_actual, f, f_prima):
    f_val = f.subs(x, x_actual)
    f_der = derivada.subs(x, x_actual)
    x_siguiente = x_actual - f_val / f_der
    return x_siguiente

inicio = float(input("Ingrese su x inicial: "))
# n = int(input("Ingrese número de iteraciones: "))
x_act = inicio

# for i in range(n):
#     resultado = formula_newton(resultado, mi_funcion, derivada)
#     print(resultado)

while True:
    x_sig = formula_newton(x_act, mi_funcion, derivada)
    if abs(x_sig-x_act) < error:
        break
    x_act = x_sig
    print(x_act)