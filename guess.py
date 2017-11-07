from random import randint

def game(random_num):
    while(True):
        guess = int(input('Input guess\n'))
        if guess < random_num:
            print('Too low, try again!')
            insultgen()
        elif guess > random_num:
            print('Too high, try again!')
            insultgen()
        elif guess == random_num:
            endgame(random_num)            

def endgame(random_num):
    r = input('You got it! Want to play again? y/n\n')
    if r == 'y':
        game(random_num)
    elif r == 'n':
        print('Thanks for playing!')

def insultgen():
    ins = ['You got it wrong, you fool!','You nincompoop, why did you type that number?','','','']
    #print (ins[1])

b = int(input('Please input a number to set the range.\n'))
random_num = randint(1,b)
print(random_num)

game(random_num)
