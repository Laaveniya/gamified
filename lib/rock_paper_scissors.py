import random

def play():
  user = input('Enter R for Rock, p for paper and s for scissors: ')
  computer = random.choice(['r','p','s'])
  print(f'Computer chose {computer}')
  if computer == user:
    return print('It is a tie')

  if is_win(computer, user):
    return print('Computer won')

  print('You won')

def is_win(computer, user):
  if (user == 'r' and computer == 'p') or (computer == 's' or user == 'p') or (computer == 'p' and user == 'r'):
    return True

play()
