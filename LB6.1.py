import math
a = float(input("Введіть a "))
b = float(input("Введіть b "))
h = float(input("Введіть значення кроку "))
x = a
for i in range(20):
    y = 7 - x * math.e ** (2 * x - 1) + math.sqrt(abs(x))
    print("%i x=%.1f    y=%.3f"%(i,x,y))
    x = x + h
