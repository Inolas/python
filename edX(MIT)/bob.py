s='adgogbobob;bajboo'
#Counter to count the number of times the word 'bob' occurs in the statement
bobcounter = 0

#for loop to point keep a pointer on every letter in the string
for pointer in range(len(s)):
    #to check whether the 3 letters from the pointer is equal to 'bob
    if(s[pointer:pointer+3] == 'bob'):
        bobcounter+=1
#printing the total number of 'bob' in the string
print ("Number of times bob occurs is: "+str(bobcounter))
