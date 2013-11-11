def lowest_payment(balance, annualInterestRate):
    ch_balance = balance
    monthly_interest = annualInterestRate / 12.0
    monthly_pay_lower = balance / 12
    monthly_pay_upper = balance * ((1 + monthly_interest) ** 12) / 12.0
    minimum_monthly_payment = 0
    while round(ch_balance, 2) != 0:
        minimum_monthly_payment = (monthly_pay_upper + monthly_pay_lower) / 2.0
        ch_balance = balance
        for month in range(1, 13):
            ch_balance -= minimum_monthly_payment
            ch_balance += (ch_balance * monthly_interest)
        if ch_balance > 0:
            monthly_pay_lower = minimum_monthly_payment
        else:
            monthly_pay_upper = minimum_monthly_payment
    print 'Lowest payment:', round(minimum_monthly_payment, 2)