from cmath import sin
import math
a = float(input("Введіть значення a: "))
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))
m = (x ** 3 + a) * (y - math.log(abs(y)) - sin(a)) + ((x **3 + y) ** (1/3))
print("Z =", m)
