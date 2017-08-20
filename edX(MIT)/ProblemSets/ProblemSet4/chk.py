import random
VOWELS='AEIOU'
CONSONANTS='QWRTYPLKJHGFDSZXCVBNM'
n=5
hand={}
numVowels = int(n / 3)
for i in range(numVowels):
    x = VOWELS[random.randrange(0,len(VOWELS))]
    hand[x] = hand.get(x, 0) + 1    
for i in range(numVowels, n):    
    x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
    hand[x] = hand.get(x, 0) + 1
        
print(hand)
