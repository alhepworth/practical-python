# pcost.py
#
# Exercise 1.27
import csv, sys


def protfolio_cost(filename):
 'Does the calcs'
 totalCost = 0
 with open(filename, 'rt') as f:
 rows = csv.reader(f)
 next(rows)
 for row in rows:
 try:
 thisCost = int(row[1]) * float(row[2])
 totalCost += thisCost
 print("thisCost is ", round(thisCost, 0))
 except ValueError:
 print("Couldn't cast")
 return totalCost

if len(sys.argv)==2:
 filename=sys.argv[1]
else:
 filename='Data/portfolio.csv'

print('filename is ',filename)
cost = protfolio_cost('Data/missing.csv')
print("cost is ", round(cost, 2))