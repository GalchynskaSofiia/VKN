import math
x = float(input("Введіть a "))
b = float(input("Введіть b "))
h = float(input("Введіть значення кроку "))
Sp = []
while x <= b:
    y = 7 - x * math.e ** (2 * x - 1) + math.sqrt(abs(x))
    Sp.append(y)
    x = x + h
print("Список = ", Sp)
