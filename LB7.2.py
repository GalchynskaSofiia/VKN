import random
m = int(input("Введіть число M: "))
n = int(input("Введіть число N: "))
def generate_random_word(length):
    for i in range(m):
       letters = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
       s1 = "".join(random.choice(letters) for i in range(length))
       print(s1, end = " ")
generate_random_word(n)
