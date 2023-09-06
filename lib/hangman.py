from words import words
import random
import string

def get_random_word(words):
  word = random.choice(words)
  while '_' in word or ' ' in word:
    word = random.choice(words)

  return word

def hangman():
  random_word = get_random_word(words).upper()
  print(random_word)
  word_letters = set(random_word)
  guessed_letters = set()
  lives = len(random_word) + 5
  alphabets = set(string.ascii_letters.upper())
  while (len(word_letters) > 0 and lives > 0):
    print(f"Word to guess {[letter if letter in guessed_letters else '_' for letter in random_word]}")
    guess = input("Please enter a letter")
    lives -= 1
    if guess in word_letters:
      guessed_letters.add(guess)
      word_letters.remove(guess)
      print(f"Guessed right! {guess} is in the word to guess and number of guesses left is {lives}")
    elif guess in guessed_letters:
      print(f"You have already guessed the letter {guess} and number of guesses left is {lives}")
    elif guess in alphabets - guessed_letters:
        print(f"Wrong guess: {guess} and number of guesses left {lives}")
    else:
      print(f'Invalid guess and number of guesses left {lives}')

  if len(word_letters) == 0:
    print(f'Yay! You guessed the word right! It is {random_word}')
  else:
    print(f'Opps You ran out of guesses! {random_word} is the right word')


hangman()
