import random
M = int(input('Введіть кількість рядків: '))
N = int(input('Введіть довжину рядка: '))
def random_row(alphabet):
    x=''
    for i in range(N):
         y = random.choice(alphabet)
         x = x + y
    return x
for i in range(M):
    print(random_row('abcdefghijklmnopqrstuvwxyz'))
