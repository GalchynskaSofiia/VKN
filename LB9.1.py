x = int(input("Введіть число: "))
spisok = [(i+1) * x for i in range(20)]
A = tuple(spisok)
print(A)
B = (A[9], A[10])
print("B = ", B)
C = (A[-3], A[-2], A[-1])
print("C = ", C)
D = (A[0], A[1], A[2], A[3])
print("D = ", D)


