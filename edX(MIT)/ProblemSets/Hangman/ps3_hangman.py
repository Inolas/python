#!/usr/bin/env python -u etc
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'rb', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    checkWord = ''
    for letters in secretWord:
        if letters in lettersGuessed:
            checkWord+= letters
        else:
            return False
    return checkWord==secretWord
'''
    secretList=[]
    for letters in secretWord:
        secretList.append(letters)
    secretList.sort()
    lettersGuessed.sort()
    print (secretList)
    return lettersGuessed==secretList

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print (isWordGuessed(secretWord,letterGuessed))
'''
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretList=list(secretWord)
    for word in secretList:
        if word in lettersGuessed:
            continue
        else:
            i=secretWord.index(word)
            secretWord = secretWord[:i]+ '_ '+secretWord[i+1:]
    return secretWord
    
#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print (getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    st=string.ascii_lowercase
    for letter in lettersGuessed:
        if(lettersGuessed.count(letter)>1):
            lettersGuessed.remove(letter)
        else:
            st=st[:st.index(letter)]+st[st.index(letter)+1:]
    return st
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print ("Available letters: "+getAvailableLetters(lettersGuessed))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guessesLeft = 8
    lettersGuessed=[]
    print ('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    while(guessesLeft>0):
        print ('-------------')
        print('You have '+str(guessesLeft)+' guesses left.')
        availableLetters=getAvailableLetters(lettersGuessed)
        print('Available letters: '+availableLetters)
        guessedLetter=input('Please guess a letter: ')
        lettersGuessed.append(guessedLetter)
        guessedWord=getGuessedWord(secretWord, lettersGuessed)
        if(guessedLetter in availableLetters and guessedLetter in secretWord):
            print ('Good guess: '+guessedWord)
            if(guessedWord is secretWord):
                print ('-------------')
                print('Congratulations, you won!')
                break
        elif(lettersGuessed.count(guessedLetter)>1):
            print ('Oops! You\'ve already guessed that letter: '+guessedWord)
        else:
            print ('Oops! That letter is not in my word: '+guessedWord)
            guessesLeft-=1
    if(guessesLeft==0):
        print ('-------------')
        print('Sorry, you ran out of guesses. The word was '+secretWord+'.')
    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'sea'
#secretWord = str(chooseWord(wordlist).lower())[2:-1]
hangman(secretWord)

