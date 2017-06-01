import random
from time import sleep

seed_num = input('Input the number of letters in your first name, this will tell you your future!')

sleep(2)

print ('Okay great! Im gathering your future,give me a few more seconds.')

sleep(4)

messages = ['You are going to become rich!',
    'Your going to get a new car in the near future!',
    'Your future is bright! Your going to be very happy!',
    'Be ready for some big changes, but positive ones!',
    'I see new opportunities coming your way!',
    'You will be seeing an increase in money soon!',
    'A possible promotion or a better job will be coming your way!'
    'Something you have been wanting, is coming!',
    'Hope you like shiny things, your going to come across a hidden tressure!']

print(messages[random.randint(0, len(messages) - 1)])
