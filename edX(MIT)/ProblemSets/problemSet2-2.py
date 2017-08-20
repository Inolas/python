balance = 3926
annualInterestRate = 0.2

totalPaid=0
previousBalance=balance

for fixedMonthlyPayment in range(0,balance,10):
    previousBalance=balance
    monthCount=0
    while(monthCount<12):
        monthlyInterestRate=annualInterestRate/12.0
        monthlyUnpaidBalance=previousBalance-fixedMonthlyPayment
        previousBalance=monthlyUnpaidBalance*(1+monthlyInterestRate)
        totalPaid+=fixedMonthlyPayment
        monthCount+=1
    if(previousBalance<0):
        print'Lowest payment: '+str(fixedMonthlyPayment)
        break