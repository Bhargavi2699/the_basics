import random
from words import words
from hangman_visuals import lives_visual_dict
import string

#some words may have some unnecessary characters such as spaces and symbols (-, _, etc).

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    #checking if the symbols are present
    while '-' in word or ' ' in word:
        #we still keep on looking for words without said symbols
        word = random.choice(words)
    
    return word.upper()

def hangman(): #keeping track of what we've guessed, correctly or not
    word = get_valid_word(words) #checking if it is a valid letter or not, hence calling the function
    #word_letters is gonna save all the letters in 'word' as a set
    word_letters = set(word) #one of the data types that store a collection of items - set
    alphabet = set(string.ascii_uppercase) #import a predertimed list of uppercase characters in a dictionary
    used_letters = set() #keep track of what the user has typed out

    lives = 7

    while len(word_letters) > 0 and lives > 0: #guessing till they reach the right answer
        #.join() turns an iterable into a string, seperated by whatever it was before .join came in. Like a space.
        print("You have", lives ,"lives/life and you have used: ", ' '.join(used_letters))
    
        #what the current word is with '_' in between
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", ' '.join(word_list))

        #getting user input
        user_input = input("Guess a letter please: ").upper()
        #if this is a valid character in the alphabet that hasn't been used yet, we will add it to the letters that have
        #already been used till now, since it is finally being used.
        if user_input in alphabet - used_letters:
            used_letters.add(user_input) #we finally add it to the letters used, since it is now finally used
            #if letter guessed is in the word, then we remove that letter from 'word_letters'
            if user_input in word_letters:
                #therefore, everytime a letter is guessed correctly, word_letter set size keeps decreasing
                word_letters.remove(user_input)
            else:
                lives -= 1            
                print("Letter", user_input, "is not present in the word")

        #if letter is already guessed, since it becomes invalid
        elif user_input in used_letters:
            print("You have already guessed this letter. Please guess another letter.")
        
        else: #if they've guessed a symbol instead
            print("Invalid input. Please enter a letter.")

    #gets here when len(word_letters) == 0 and lives == 0
    if lives == 0:
        print("Sorry, you have died. The word was", word, "!!")
        print(lives_visual_dict[lives])
    else:
        print("You guessed the word",word ,"correctly!!")

if __name__ == "__main__":
    hangman()

