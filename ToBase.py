from string import digits, ascii_uppercase


def ToBase(n, base):
    """
    Функция принимает на вход два числа формата int():
    n - число которое нужно перевести из 10 в другую Систему счисления
    base - число основание этой системы счисления

    На выходе: изначальное число, но в нужной системе счисления
    """
    alph = digits + ascii_uppercase
    res = ''
    while n > 0:
        res += alph[n % base]
        n //= base
    return res[::-1]
