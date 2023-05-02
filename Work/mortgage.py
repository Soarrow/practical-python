# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_start_month = int(input('Enter which month you want to start extra payments: '))
extra_end_month = int(input('Enter which month you want to end extra payments: '))
extra_payment = int(input('Enter extra payment amount: '))
month = 0;

while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if (month > extra_start_month and month <= extra_end_month):
        principal -= extra_payment
        total_paid += extra_payment


print('Total paid', total_paid)
print('Month', month)