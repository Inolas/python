high = 100
low=0

print "Please think of a number between 0 and 100!"
while(True):
    mid=(high+low)/2
    print "Is your secert number "+str(mid)+"?"
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",
    guess=raw_input()
    if(guess=='l'):
        low = mid
    elif(guess=='h'):
        high = mid
    elif(guess=='c'):
        print "Game over. Your secret number was: "+str(mid)
        break
    else:
        print "Sorry, I did not understand your input."

