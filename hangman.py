# Problem Set 2, hangman.py
# Name: Baranivska Valeria
# Collaborators: a bit of Savchuk's work 
# Time spent: nearly 4 days

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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
    print(len(wordlist), "words loaded.")
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
    letters_guessed = set(letters_guessed)
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_guessed = set(letters_guessed)
    print_letter = ''
    for i in secret_word:
        if i in letters_guessed:
            print_letter += i
        else:
            print_letter += ' _ '
    return print_letter

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = set(string.ascii_lowercase)
    for i in letters_guessed:
        letters.remove(i)
    return ''.join(sorted(letters))

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
    
    letters_guessed = []
    sep_text = '-' * 15
    guesses_remaining = 6
    warnings_remaining = 3
    
    print('Welcome to the game Hangman!\n',f'I am thinking of a word that is {len(secret_word)} letters long.')
    
    while guesses_remaining != 0 and not is_word_guessed(secret_word,letters_guessed):
        fl = True
        print(sep_text,'\n',f'You have {guesses_remaining} guesses left.\n',f'Available letters:{get_available_letters(letters_guessed)}')

        user_input = input('Please guess a letter: ').lower()

        if len(user_input) != 1:
            print('Something go wrong...')
            fl = False
        elif user_input not in string.ascii_lowercase:
            print('Not available symbol')
            fl = False
        elif user_input in letters_guessed:
            print("Oops! You've already guessed that letter.")
            fl = False
        else:
            letters_guessed.append(user_input)
            if user_input in secret_word:
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                if user_input in {'a', 'i', 'e', 'o', 'u'}:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))

        if fl == False:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f'You have {warnings_remaining} warnings: ',get_guessed_word(secret_word, letters_guessed))
                
            else:
                guesses_remaining -= 1
                print('You have no warnings left so you lose one guess: ',get_guessed_word(secret_word, letters_guessed))
        
           
    print(sep_text)
    if guesses_remaining != 0:
        print('Congratulations, you won!')
        print('Your total score for this game is: ', guesses_remaining * len(set(secret_word)))
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

    pass
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
    for w in other_word:
        if len(my_word) != len(w):
            return False
        

    set_word = set(my_word.replace(' _ ', ''))
    if not set_word.issubset(set(other_word)):
        return False
    else:
        for i, j in zip(my_word, other_word):
            if i == ' _ ':
                if j in setA:
                    return False
            elif i != j:
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
             
    matching_words = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            matching_words.append(i)
    if matching_words:
        print(*matching_words)
    else:
        print('No matches found')
        

   
   
                     
    
    


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
    
    letters_guessed = []
    sep_text = '-' * 20
    guesses_remaining = 6
    warnings_remaining = 3
    
    print('Welcome to the game Hangman!\n',f'I am thinking of a word that is {len(secret_word)} letters long.')
    
    while guesses_remaining != 0 and not is_word_guessed(secret_word,letters_guessed):
        fl = True
        print(sep_text,'\n',f'You have {guesses_remaining} guesses left.\n',f'Available letters:{get_available_letters(letters_guessed)}')
   
        user_input = input('Please guess a letter: ').lower()
        
        if len(user_input)>1:
            print('Oops! Not available symbol')
            fl = False
        elif user_input == '':
            print('Oops! Not available symbol')
            fl = False
        elif user_input == '*':
            print('Possible word matches are:',show_possible_matches(get_guessed_word(secret_word, wordlist)))
        elif user_input not in string.ascii_lowercase:
            print('Oops! Not available symbol')
            fl = False
        elif user_input in letters_guessed:
            print("Oops! You've already guessed that letter.")
            fl = False
        else:
            letters_guessed.append(user_input)
            if user_input in secret_word:
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                if user_input in {'a', 'i', 'e', 'o', 'u'}:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))

        if fl == False:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f'You have {warnings_remaining} warnings: ',get_guessed_word(secret_word, letters_guessed))
                
            else:
                guesses_remaining -= 1
                print('You have no warnings left so you lose one guess: ',get_guessed_word(secret_word, letters_guessed))
           
    print(sep_text)
    while True:
        if guesses_remaining != 0:
            print('Congratulations, you won!')
            print('Your total score for this game is: ', guesses_remaining * len(set(secret_word)))
            break
        elif guesses_remaining == 0 :
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
            break 

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
