mn = set()
for i in range(-34, 0):
    if (-1 * i) % 10 == 4 and (-1 * i) % 4 != 0:
        mn.add(i)
for i in range(0,45):
    if i % 10 == 4 and i % 4 != 0:
        mn.add(i)
print(sorted(mn))

