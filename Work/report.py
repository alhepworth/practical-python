# report.py
#
# Exercise 2.4
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/amh/PycharmProjects/practical-python', '/Users/amh/PycharmProjects/practical-python/Work'])


import fileparse

# import sys
# sys.path.append('/Users/amh/PycharmProjects/practical-python/Work')


def read_portfolio(filename):
 '''Computes the total cost (shares*price) of a portfolio file'''
 with open(filename) as lines:
  portfolio = fileparse.parse_csv(lines,select=['name','shares','price'], types=[str,int,float])
  return portfolio

def read_prices(filename):
 ''' reads a set of prices into dict '''
 with open(filename) as lines:
  prices = dict(fileparse.parse_csv(lines,types=[str,float],has_headers=False))
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

def main(args):
 if len(args) != 3:
  raise SystemExit('Usage: %s portfile pricefile' % args[0])
 portfolio_report(args[1], args[2])

if __name__=='__main__':
 import sys
 main(sys.argv)