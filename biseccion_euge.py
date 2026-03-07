def f(x):
    return 4*x**5 + 2*x**3 + 7*x + 27

def signo(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1
    
def biseccion(a, b, error):
    if f(a)*f(b) < 0 and a < b:
        while b-a > error:
            c = (a+b)/2
            if f(c) == 0:
                return c
            elif signo(f(a))*signo(f(c)) < 0:
                b = c
            else:
                a = c
        return c


print(biseccion(-3, -1, 0.001))
