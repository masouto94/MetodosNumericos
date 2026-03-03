def f(x):
    return x**2 + 3*x - 20

def signo(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1

a = float(input("Extremo mínimo:"))
b = float(input("Extremo máximo:"))
error = float(input("Máximo error tolerado:"))

def biseccion(a, b, error):
    if signo(f(a))*signo(f(b)) >= 0:
        print("El intervalo no contiene una raíz")
        return None
    while (b-a) > error:
        c = (a+b) / 2
        if f(c) == 0:
            return c
        if signo(f(a))*signo(f(c)) < 0:
            b = c
        else:
            a = c
    return c
    
def triseccion(a, b, error):
    c1 = a + (b-a)/3
    c2 = b - (b-a)/3
    if signo(f(a)) == signo(f(b)) == signo(f(c1)) == signo(f(c2)):
        print("El intervalo no contiene una raíz")
        return None
    while (b-a) > error:
        c1 = a + (b-a)/3
        c2 = b - (b-a)/3
        if f(c1) == 0:
            return c1
        if f(c2) == 0:
            return c2
        if signo(f(a))*signo(f(c1)) < 0:
            b = c1
        elif signo(f(a))*signo(f(c2)) < 0:
            b = c2
        else:
            a = c2
    return (c1+c2)/2
    

print(triseccion(a, b, error))