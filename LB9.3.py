Sl = {}
for i in range(9):
    key = input("Введіть назву металу: ")
    value = int(input("Введіть густину металу (в кг/м^3): "))
    Sl[key] = value
print(Sl)
print(dict(sorted(Sl.items())))
print(dict(sorted(Sl.items(), reverse = True, key = lambda x: x[1])))
Sl_1 = list(Sl.items())
print(Sl_1[4])
