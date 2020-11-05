# mortgage.py
#
# Exercise 1.7
principal = 500000
rate=0.05
payment=2684.11
total_paid=0.0
month=0
extra_payment_start_month=5*12+1
extra_payment_end_month=9*12
extra_payment=1000
while principal>0:
 month = month + 1
 if month>=extra_payment_start_month and month<=extra_payment_end_month:
  month_payment = payment + extra_payment
 else:
  month_payment = payment
  principal=principal*(1+rate/12)-month_payment
  total_paid=total_paid+month_payment
 print(f'{month} {total_paid:0.2f} {principal:0.2f}')
print(f'Total paid {total_paid:0.0f} over {month} months')