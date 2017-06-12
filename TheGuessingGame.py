"""The Guessing Game"""

from time import sleep

import random

print ('!!!!!!!!!!Welcome to the Guessing Game!!!!!!!!!!')
sleep (2)
print ('You will get 5 chances to guess what number Im thinking about!')
sleep (3)
print ('Hope you dont!')
sleep (1)
print ('WAIT FOR IT!!!!!!')
sleep (2)
print ('Waittt.....')
sleep (2)
print ('██████▌▄▌▄▐▐▌███▌▀▀██▀▀')
print ('████▄█▌▄▌▄▐▐▌▀███▄▄█▌')
print ('▄▄▄▄▄██████████████▀')
sleep (2)
print ('LOL!Good Luck! ^.^')
sleep (4)
print ('Pick a number between 1-99, type it, and push Enter.')
n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99:"))
while 5 != "guess":
    print ('Guess is low')
    guess = int(raw_input("Enter an integer from 1 to 99:"))
elif guess > "34":
    print ('Guess is high')
    guess = int(raw_input("Enter an integer from 1 to 99:"))
else:
    print ('You guessed it!')
