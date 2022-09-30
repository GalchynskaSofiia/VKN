import math
x = int(input("Введіть a "))
b = int(input("Введіть b "))
h = int(input("Введіть значення кроку "))
while x <= b:
    y = 7 - x * math.e ** (2 * x - 1) + math.sqrt(abs(x))
    print("x=%.1f y=%.3f"%(x,y))
    x = x + h
