import csv
import pandas as pd
from tabulate import tabulate
numb = []
columns = ['', 'month', 'amount os sales']
with open('lab11.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        numb.append(int(row['amount']))
df = pd.read_csv('lab11.csv', delimiter=',')
print(tabulate(df, headers = columns))
print("total amount: ", sum(numb))
print("mean: ", int(sum(numb)/3))
file.close()
