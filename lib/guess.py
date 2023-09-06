import random

def guess(x):
  r = random.randint(1, x)

  guess = 0

  while(guess != r):
    guess = int(input('Input your guess: '))
    if guess == r:
      print('Yay! You are right!')
    elif guess > r:
      print('Your guess is bigger the game number')
    elif guess < r:
      print('Your guess is lesser the game number')


def computer_guess(x):
  low = 0
  high = x
  print(x)
  guess = random.randint(low, high)

  reply= ''
  while(reply != 'c'):
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low
    print(f' My guess is {guess}')
    reply = input(f'On this guess {guess} Press c if correct, l if too low or h if too high: ')
    if reply == 'l':
      low = guess + 1
    elif reply == 'h':
      high = guess - 1
  print(f'Yay! Your guess {guess} is right!')

guess(10)
