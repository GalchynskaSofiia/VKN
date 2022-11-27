import random
N = int(input("Кількість номерів: "))
for i in range(N):
    def random_number():
        x = str(random.randint(1000000,9999999))
        print("099" + x)
    random_number()

