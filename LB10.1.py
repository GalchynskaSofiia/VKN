import re
x = open('text.txt', 'r')
x = x.read().lower()
y = re.findall(r'she', x)
f = re.findall(r'was', x)
chastota = {}
for word in y:
    count = chastota.get(word, 0)
    chastota[word] = count + 1
for word in f:
    count = chastota.get(word, 0)
    chastota[word] = count + 1
g = open('freq.txt', 'w')
for key in chastota:
    g.write(key + '=' + str(chastota[key]) + '\n')
g.close()
