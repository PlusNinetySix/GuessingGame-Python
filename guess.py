import random
from random import randint

def randgen():
    b = int(input('Please input a number to set the range.\n'))
    randnum = randint(1,b)
    return randnum

def game(randnum):
    win = False
    while not win:
        guess = int(input('Input guess\n'))
        if guess < randnum:
            print('Too low, try again!')
            insultgen()
        elif guess > randnum:
            print('Too high, try again!')
            insultgen()
        else:
            print('Got it!')
            win = True

def insultgen():
    ins = ['You got it wrong, you fool!','You clod, why did you type that number?','You'"'re not very bright.",'How did you get that number? It'"'s not even close.",'I honestly do not know how you even got that number...']
    print (random.choice(ins))

playagain = True
while playagain:
    game(randgen())
    p = input('Want to play again? y/n\n')
    if p =='y':
        playagain = True
    else:
        print('Thanks for playing!')
        playagain = False
