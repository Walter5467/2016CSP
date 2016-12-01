from __future__ import print_function
import random

def validate():
    guess = '1' #initialization with bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
    


def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''This function is to have the user guess who is the winner
    The function will choose a random player in players
    It will have the user guess through raw input and it will also show how many guesses the user has made
    '''
    winner = random.choice(players)
    
    
    #The code below will show how many players are left after one has been chose
    
    print('Guess which of these people won the lottery: ')
    for p in players[:len(players)-1]: # for every player in players it will subtract 1 from the total players
        print(p+', ')
    print(players[len(players)-1]) # Will print the length of players but subtract 1 
    
    '''
    This will show how many guesses you have taken so far
    '''
    guesses = 1
    while raw_input() != winner:
        print('Guess again!')
    guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses

def goguess():
    print('I have a number between 1 and 20 inclusive')    
    answer = random.randint(1,20)
    guesses = 1
    guess = int(raw_input('Guess: '))
    while guess != answer:
        if guess > answer:
            print('Too high!')
            guesses += 1
        else:
            print('Too low!')
            guesses += 1
        guess = int(raw_input('Guess: '))   
    print('Correct!')
    print('Amount of guesses:', guesses)
    
        