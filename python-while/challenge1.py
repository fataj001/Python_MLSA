# Tried Version
import random
guess = 0
number = 0



while guess != 5:
  guess = input('Guess a number between 1 to 5: ')
  number = number + 1

  guess = random.randint(1, 5)



print(f'You guessed it in {number} tries.')


# Solution
import random

value = random.randint(1, 5)
count = 0
guess = 0
while guess != value:
    count += 1
    guess = input('Guess a number between 1 and 5: ')
    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'You guessed it in {count} tries!')