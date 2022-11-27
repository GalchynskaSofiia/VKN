import json
inform = '{"gold": 2070, "silver": 25, "palladium": 2147, "platinum": 1170}'
inform_dict = json.loads(inform)
with open('lab11.txt', 'w') as json_file:
    inf = json.dump(inform_dict, json_file)
metal = input("Оберіть назву металу, з якого зроблено виріб (gold, silver, palladium, platinum): ")
x = int(input("Введіть масу виробу (у грамах): "))
y = inform_dict[metal]
print("Ціна виробу становить", x * y, "грн")