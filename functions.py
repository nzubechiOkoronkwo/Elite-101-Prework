import random
import spiderDraw



# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
#Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.
def check_word(the_word: str, guess: str, correct_guesses: list, incorrect_guesses: list):
  if len(guess) > 1:
    print()
    print('One letter at a time please')
    print()
    return 
    
  if not guess.isalpha(): 
    print()
    print('Looks like you typed something that\'s not a letter. Let\'s get serious')
    print()
    return
    
  if guess in correct_guesses or guess in incorrect_guesses:
    print()
    print('Uh oh. You already guessed this letter before.')
    print()
    return
    
  if guess in the_word:
    print()
    print('Excellent guess!')
    print()
    correct_guesses.append(guess)
    return
    
  else:
    print()
    print('Sorry. Not in the word')
    print()
    incorrect_guesses.append(guess)
    return 
    
    




# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(the_word, correct_guesses):
  progress = ''
  for letter in the_word:
    if letter in correct_guesses:
      progress += letter
    else:
      progress += '_'
  return progress
  



# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(number_of_incorrect_guesses):
  draw_function = spiderDraw.progressive_spider_drawings[number_of_incorrect_guesses]
  draw_function()

  
    



#Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.

def generate_word():                                #Line #1
  wordList = open('words.txt').read().split()             #2
  word = random.choice(wordList)                          #3
  print('Word = ' + '_ '*len(word))                       #4
  return word                                             #5
  pass


  

#Put the introduction code/input player name into here 
def introduction():
  name = input("What's your name, victim? ")
  print(
    f'''
Welcome to the Spooky Spider game, {name}.
    
    ''')
