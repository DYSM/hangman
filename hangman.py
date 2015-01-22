#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
*========*''', '''

  +---+
  |   |
  O   |
      |
      |
      |
*========*''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
*========*''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
*========*''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
*========*''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
*========*''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
*========*''']

def calcPoint(record):
    record += 10
    return record

def readWordList():
    file = open('text.txt', 'r')
    return file.readline().split()

def readRecord():
    file = open('record.txt', 'r')

    list=file.readline().split()
    if(len(list) == 0):
        return ['none', 0]
    else:
        return list

def writeRecord(name, record):
    file = open('record.txt', 'w')
    file.write(name+" "+str(record))
    file.close()

words = readWordList()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = ''
    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks += secretWord[i]
        else:
            blanks += '_'

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# Check if the player has won
def checkCorrectAnswer(correctLetters, secretWord):
    foundAllLetters = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
    return foundAllLetters

# Check if player has guessed too many times and lost
def checkWrongAnswer(missedLetters, secretWord):
    # Check if player has guessed too many times and lost
    if len(missedLetters) == len(HANGMANPICS) - 1:
        return True
    return False
            
def main():
    """Main application entry point."""

    print('H A N G M A N - DYSM')

    name = readRecord()[0]
    highRecord = int(readRecord()[1])

    print('Highest Record is:', name + " - " + str(highRecord))

    record = 0
    missedLetters = ''
    correctLetters = ''
    gameSucceeded = False
    gameFailed = False
    secretWord = getRandomWord(words)

    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

        if gameSucceeded or gameFailed:
            if gameSucceeded:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                record = calcPoint(record)
            else:
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')

            # Ask the player if they want to play again (but only if the game is done).
            print("Now score : ", record)
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameSucceeded = False
                gameFailed = False
                secretWord = getRandomWord(words)
                continue 
            else:
                if(highRecord < record):
                    writeRecord(input("NEW RECORD!!\nWhat's your name?: "), record)
                break

        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)
        if guess in secretWord:
            correctLetters = correctLetters + guess
            gameSucceeded = checkCorrectAnswer(correctLetters, secretWord)
        else:
            missedLetters = missedLetters + guess
            gameFailed = checkWrongAnswer(missedLetters, secretWord)


if __name__ == "__main__":
    main()