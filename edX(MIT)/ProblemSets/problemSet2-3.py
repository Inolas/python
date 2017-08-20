balance = 320000
annualInterestRate = 0.2

totalPaid=0
monthlyInterestRate=annualInterestRate/12.0
LowerBound=balance/12
UpperBound=(balance*(1+monthlyInterestRate)**12)/12.0
while(True):
    mid=(LowerBound+UpperBound)/2
    previousBalance=balance
    for month in range(0,12):
        monthlyUnpaidBalance=previousBalance-mid
        previousBalance=monthlyUnpaidBalance*(1+monthlyInterestRate)*1.0
    if previousBalance > 0:
        LowerBound = mid
    if previousBalance < 0:
        UpperBound = mid
    if abs(previousBalance) < 0.01:
        print'Lowest payment: '+str(round(mid,2))
        break
