# pcost.py
#
# Exercise 1.27
import csv, sys
import sys
sys.path.append('/Users/amh/PycharmProjects/practical-python/Work/')
import report

def protfolio_cost(filename):
 'Does the calcs'
 portfolio = report.read_portfolio(filename)
 return sum([s['shares'] * s['price'] for s in portfolio])

if len(sys.argv)==2:
 filename=sys.argv[1]
else:
 filename='Data/portfolio.csv'

print('filename is ',filename)
cost = protfolio_cost('Data/missing.csv')
print("cost is ", round(cost, 2))