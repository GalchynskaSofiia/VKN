import random
import numpy as np
N = int(input("Введіть кількість елементів N: "))
a = int(input("Введіть перше значення діапазону: "))
b = int(input("Введіть друге значення діапазону: "))
masiv1 = np.random.randint(a,b,N)
masiv2 = np.power(3, masiv1)
masiv = np.append(masiv1, masiv2)
print(sorted(masiv))

