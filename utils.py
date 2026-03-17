# Fuerzo que al dividir por cero tire error
def div(num, den):
    if den.is_zero:
        raise ZeroDivisionError("División por cero")
    return num / den


from sympy import Symbol

SYMBOLS = {symbol: Symbol(symbol) for symbol in list("abcdefghijklmnopqrstuvwxyz")}
