#This number game stores a random number and the user will get the chance to guess that random number
import random

def guess(x):
  random_number = random.randint(1, x)
  guess = 0;
  while (guess != random_number):
    guess = int(input(f'Guess a number from 1 and {x}: '))
    if guess < random_number:
      print('Too low')
    elif guess > random_number:
      print('Too high')
  print ('Passed')

print("What is the range of the guessed number? Type in an integer: ")
range = int(input())
guess(range)