# report.py
#
# Exercise 2.4

import csv
import sys
sys.path.append('/Users/amh/PycharmProjects/practical-python/Work')
import fileparse



def read_portfolio(filename):
 '''Computes the total cost (shares*price) of a portfolio file'''
 portfolio = parse_csv(filename,select=['name','shares','price'], types=[str,int,float])
 return portfolio

def read_prices(filename):
 ''' reads a set of prices into dict '''
 prices = dict(parse_csv(filename,types=[str,float],has_headers=False))
 '''
 prices = {}
 f=open('Data/prices.csv','r')
 rows=csv.reader(f)
 for row in rows:
  if len(row) > 0:
   prices[row[0]] = float(row[1])
 '''
 return prices

def calc_gain():
 portfolio=read_portfolio('Data/portfolio.csv')
 prices=read_prices('Data/prices.csv')
 gain=0
 for portitem in portfolio:
  name = portitem['name']
  gain += prices[name] - (portitem['shares'] * portitem['price'])
 return gain

def make_report(portfolio, prices):
 listchange = []
 for portitem in portfolio:
  name = portitem['name']
  change = prices[name] - portitem['price']
  s = (name, portitem['shares'], prices[name], change)
  listchange.append(s)
 return listchange

def portfolio_report(portfolio_file, prices_file):
 portfolio = read_portfolio(portfolio_file)
 prices = read_prices(prices_file)
 report=make_report(portfolio,prices)
 headers = ('Name', 'Shares', 'Price', 'Change')
 print('%10s %10s %10s %10s' % headers)
 print('---------- ---------- ---------- -----------')
 for name, shares, price, change in report:
  print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

portfolio_report('Data/portfolio.csv','Data/prices.csv')