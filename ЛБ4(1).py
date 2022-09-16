import math
x = float(input("Введіть значення x: "))
a = math.cos(abs(x ** 3 - 4))
b = math.log(abs(x))
c = (x - 8 + (x ** 2)) ** (1/3)   # знаменник
print((a + b) / c)
