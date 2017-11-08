import random
from random import randint

def randgen(): #generates a random number
    b = int(input('Please input a number to set the range.\n'))
    randnum = randint(1,b)
    #print(randnum) #displays number chosen. used for debugging purposes
    return randnum

def game(randnum): #the actual function for the game
    win = False
    while not win:
        guess = int(input('Input guess\n'))
        if guess < randnum: #checks if the guess is lower than the generated number
            print('Too low, try again!')
            insultgen()
        elif guess > randnum: #checks if the guess is higher than the generated number
            print('Too high, try again!')
            insultgen()
        else: #if the guess is equal to the generated number, then sets the win bool to True
            print('Got it!')
            win = True

def insultgen(): #chooses from five different insults and displays a random one
    ins = ['You got it wrong, you fool!','You clod, why did you type that number?','You'"'re not very bright.",'How did you get that number? It'"'s not even close.",'I honestly do not know how you even got that number...']
    print (random.choice(ins))

playagain = True #readies to ask the user if they want to continue
while playagain:
    game(randgen()) #calls the function for the game, along with the number generation function to choose a new number
    p = input('Want to play again? y/n\n')
    if p =='y':
        playagain = True #the user can now play again
    else:
        print('Thanks for playing!')
        playagain = False #the game ends
