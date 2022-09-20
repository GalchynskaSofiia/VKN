import math
def func1(x1, x2, x3):
    m = (x1 ** 3 + x2) * (x3 - math.log(abs(x3)) - math.sin(x2)) + ((x1 **3 + x3) ** (1/3))
    return(m)
a = float(input("Введіть значення a: "))
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))
m = func1(x, a, y)
print("Z =", m)
