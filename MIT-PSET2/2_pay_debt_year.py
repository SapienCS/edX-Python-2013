month = 1
payments = 0
while month <= 12:
    print 'Month: ', month
    minimum_monthly_payment = balance * monthlyPaymentRate
    monthly_interest = annualInterestRate / 12.0
    print 'Minimum monthly payment:', round(minimum_monthly_payment, 2)
    balance -= minimum_monthly_payment
    balance += (balance * monthly_interest)
    print 'Remaining balance:', round(balance, 2)
    payments += minimum_monthly_payment
    month += 1

print 'Total paid:', round(payments, 2)
print 'Remaining balance:', round(balance, 2)
