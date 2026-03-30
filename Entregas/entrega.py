# Este programa busca aproximaciones a una raíz de una función dada a través de dos métodos:
# trisección (en primera instancia) y Newton (para aproximar mejor).


import sympy as sp

x = sp.Symbol('x')

# Funciones básicas
def f(x):
    return 5*x**4 + 2*x**3 + 7*x - 2

def signo(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

mi_funcion = f(x)
derivada = sp.diff(mi_funcion, x)


# Método de trisección
def triseccion(a, b, error):
    if f(a)*f(b) < 0 and a < b:
        while b-a > error:
            c1 = a + (b-a)/3
            c2 = b - (b-a)/3
            if f(c1) == 0:
                return c1
            if f(c2) == 0:
                return c2
            if signo(f(a))*signo(f(c1)) < 0:
                b = c1
            elif signo(f(b))*signo(f(c2)) < 0:
                a = c2
            else:
                a = c1
                b = c2
        return (c1+c2)/2
    else:
        print("Por favor, busque otros dos valores.")


# Método de Newton
def formula_newton(x_actual, f, f_prima):
    f_val = f.subs(x, x_actual)
    f_der = derivada.subs(x, x_actual)
    x_siguiente = x_actual - f_val / f_der
    return x_siguiente


#Programa principal
print(f"Este programa tiene como objetivo hallar una aproximación de una raíz de la función {f(x)}.")
print("Primero se utilizará el método de trisección. Para ello, debe ingresar dos valores aleatorios, entre los cuales se buscará una raíz.")
valor_1 = float(input("Ingrese el primer valor: "))
valor_2 = float(input("Ingrese el segundo valor (mayor al anterior): "))
primera_aproximacion = triseccion(valor_1, valor_2, 0.5)
print("Primera aproximación con trisección y un error de 0.5:", primera_aproximacion)

error = 0.01
x_act = primera_aproximacion

while True:
    x_sig = formula_newton(x_act, mi_funcion, derivada)
    if abs(x_sig-x_act) < error:
        break
    x_act = x_sig
    
print("Segunda aproximación con Newton y un error de 0.01:", x_act)