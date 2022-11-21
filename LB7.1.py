s = str(input("Введіть рядок слів: "))
s1 = s.replace(",", " ")
a = max(s1.split(), key = len)
b = min(s1.split(), key = len)
print("Довжина найбільшого слова: ", len(a))
print("Довжина найкоротшого слова: ", len(b))


