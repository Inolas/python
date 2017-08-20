balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthCount=0
totalPaid=0
previousBalance=balance
while(monthCount<12):
    monthlyInterestRate=annualInterestRate/12.0

    minimumMonthlyPayment=monthlyPaymentRate*previousBalance

    monthlyUnpaidBalance=previousBalance-minimumMonthlyPayment

    previousBalance=monthlyUnpaidBalance*(1+monthlyInterestRate)

    totalPaid+=minimumMonthlyPayment
    
    monthCount+=1
    
    print ("Month: " +str(monthCount))
    print ("Minimum monthly payment: "+str(round(minimumMonthlyPayment,2)))
    print("Remaining balance :"+ str(round(previousBalance,2)))
print("Total paid: "+str(round(totalPaid,2)))
print("Remaining balance: "+str(round(previousBalance,2)))
