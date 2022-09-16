import sys
num1 = int(input("Введіть чотиризначне число"))
a = num1 // 1000
b = num1 // 100 % 10
c = num1 % 100 // 10
d = num1 % 10
print(a + b + c + d)
