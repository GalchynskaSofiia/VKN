import numpy as np
import math
N = int(input("Введіть число: "))
if math.sqrt(N) % 1 != 0:
    n = int(math.ceil(math.sqrt(N)))
elif math.sqrt(N) % 1 == 0:
    n = int(math.sqrt(N))
A = np.arange(1,n ** 2 + 1,1)
A.shape = (n,n)
print(A)
