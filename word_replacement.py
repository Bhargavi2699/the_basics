#mainly to see replace method in python
#it takes a string, replaces some words in the string, with another.
#remember that the next time you run it, it does not get permanently replaced.
def replace_word():
    str = 'Hey guys, Bhargavi here. Hello Hello Hello'
    word_replace = input("Enter the word you want to replace: ")
    replacement_word = input("Enter your replacement word: ")
    print(str.replace(word_replace, replacement_word))

replace_word()