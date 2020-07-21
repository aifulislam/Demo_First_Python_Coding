#Guessing Game---------------

from random import randint
for x in range(1,10):
    guessNumber = int(input("Enter any guess Number between 1 to 10 : "))
    randomNumber = randint(1,10)
    if guessNumber == randomNumber:
        print('You have won')
    else:
        print('You have lost')
        print('Your random number was',randomNumber)

#Guessing Game---------------
from random import randint
for i in range(1,10):
    guessNumber = int(input("Enter any Guess Number between 1 to 10 : "))
    randomNumber = randint(1,10)
    if guessNumber == randomNumber:
        print('You have won')
    else:
        print('You have lost')
        print('Your random number was',randomNumber)

#Guessing Game---------------
import random
for i in range(1,10):
    guessNumber = int(input("Enter any Guess number between 1 to 10 : "))
    randomNumber = random.randint(1,10)
    if guessNumber == randomNumber:
        print("You have won.")
    else:
        print("You have lost.")
        print("Your Random number was :",randomNumber)

