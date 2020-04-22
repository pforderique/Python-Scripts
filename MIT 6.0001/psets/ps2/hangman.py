# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "C:\\Users\\fabri\\OneDrive\\Documents\\myPythonCodes\\MIT 6.0001\\psets\\ps2\\words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = ""
    for i in range(len(secret_word)):
      if secret_word[i] not in letters_guessed:
        word += "_ "
      else:
        word += secret_word[i]
    return word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    wordsleft = ""
    for letter in string.ascii_lowercase:
      if letter not in letters_guessed:
        wordsleft += letter
    return wordsleft

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %s letters long" % len(secret_word))
    guessesLeft = 6
    warningsLeft = 3
    letters_guessed = []
    vowels = ['a','e','i','o','u']
    while guessesLeft > 0 and not is_word_guessed(secret_word, letters_guessed):
      print("-------------------------")
      print("You have %s guesses left" % guessesLeft)
      print("Available letters:", get_available_letters(letters_guessed))
      guess = str.lower(input("Please guess a letter: "))
      while not str.isalpha(guess) or len(guess) != 1 or guess in letters_guessed:
        warningsLeft -= 1
        if(warningsLeft > 0):
          if(guess in letters_guessed):
            print("Oops! You've already guessed that letter. You now have",warningsLeft,"warnings:",get_guessed_word(secret_word,letters_guessed))
          else:
            print("Oops! That is not a valid letter. You have",warningsLeft,"warnings left:",get_guessed_word(secret_word,letters_guessed))
        elif warningsLeft == 0:
          print("You have run out of warnings. One guess was removed.")
          guessesLeft-=1
          if guessesLeft == 0:
            break
        else:
          if(guess in letters_guessed):
            print("Oops! You've already guessed that letter. You now have 0 warnings:",get_guessed_word(secret_word,letters_guessed))
          else:
            print("Oops! That is not a valid letter. You have 0 warnings left:",get_guessed_word(secret_word,letters_guessed))
        guess = str.lower(input("Please guess a letter: "))
      letters_guessed.append(guess)
      if guess in secret_word:
        print("Good guess:",get_guessed_word(secret_word,letters_guessed))
      elif guess in vowels:
        print("Oops! That vowel is not in my word. You lose 2 guesses:",get_guessed_word(secret_word,letters_guessed))
        guessesLeft-=2
      else:
        print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
        guessesLeft-=1
    if guessesLeft < 1:
      print("-------------------------")
      print("Game Lost. Secret word was",secret_word)
    else:
      score = guessesLeft*len(set(secret_word))
      print("-------------------------")
      print("You won! Your score is:",score)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_no_spaces = my_word.replace(" ","")
    if len(my_word_no_spaces) != len(other_word):
      return False
    for i in range(len(my_word_no_spaces)):
      if my_word_no_spaces[i] != "_" and my_word_no_spaces[i] != other_word[i]:
        return False
      if my_word_no_spaces[i] == "_" and other_word[i] in my_word_no_spaces:
        return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possibleWords = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        possibleWords.append(word)
    if len(possibleWords) == 0:
      print("No matches found")
    else:
      print(possibleWords)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("\n**********************************")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %s letters long" % len(secret_word))
    guessesLeft = 6
    warningsLeft = 3
    letters_guessed = []
    vowels = ['a','e','i','o','u']
    while guessesLeft > 0 and not is_word_guessed(secret_word, letters_guessed):
      print("-------------------------")
      print("You have %s guesses left" % guessesLeft)
      print("Available letters:", get_available_letters(letters_guessed))
      guess = str.lower(input("Please guess a letter: "))
      while not str.isalpha(guess) or len(guess) != 1 or guess in letters_guessed:
        if guess == "*":
          break
        warningsLeft -= 1
        if(warningsLeft > 0):
          if(guess in letters_guessed):
            print("Oops! You've already guessed that letter. You now have",warningsLeft,"warnings:",get_guessed_word(secret_word,letters_guessed))
          else:
            print("Oops! That is not a valid letter. You have",warningsLeft,"warnings left:",get_guessed_word(secret_word,letters_guessed))
        elif warningsLeft == 0:
          print("You have run out of warnings. One guess was removed.")
          guessesLeft-=1
          if guessesLeft == 0:
            break
        else:
          if(guess in letters_guessed):
            print("Oops! You've already guessed that letter. You now have 0 warnings:",get_guessed_word(secret_word,letters_guessed))
          else:
            print("Oops! That is not a valid letter. You have 0 warnings left:",get_guessed_word(secret_word,letters_guessed))
        guess = str.lower(input("Please guess a letter: "))
      letters_guessed.append(guess)
      if guess in secret_word:
        print("Good guess:",get_guessed_word(secret_word,letters_guessed))
      elif guess in vowels:
        print("Oops! That vowel is not in my word. You lose 2 guesses:",get_guessed_word(secret_word,letters_guessed))
        guessesLeft-=2
      elif(guess == "*"):
          print("Hint used. Possible word matches are:")
          show_possible_matches(get_guessed_word(secret_word,letters_guessed))
      else:
        print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
        guessesLeft-=1
    if guessesLeft < 1:
      print("-------------------------")
      print("Game Lost. Secret word was",secret_word)
    else:
      score = guessesLeft*len(set(secret_word))
      print("-------------------------")
      print("You won! Your score is:",score)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = "apple" #choose_word(wordlist)
    hangman_with_hints(choose_word(wordlist))