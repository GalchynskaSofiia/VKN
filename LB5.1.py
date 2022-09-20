import math
x = float(input("Введіть значення x: "))
def f1(x1):
    rez = x1 + 2 ** (x1 - 4) - math.sqrt(x1)
    return(rez)
def f2(x2):
    rez = math.sin(x2 * 2) + math.log10(abs(x2))
    return(rez)
def f3(x3):
    rez = math.cos(3 * x3) - 1 / x3
    return(rez)
y = 0.0
if x >= 0:
    y = f1(x)
if x > -7.7 and x < 0:
    y = f2(x)
if x <= -7.7:
    y = f3(x)
print(y)

