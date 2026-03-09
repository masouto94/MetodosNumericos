def f(x):
    return 5*x**4 + 2*x**3 + 7*x - 2

def signo(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1
    
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


print(triseccion(-3, -1, 0.001))