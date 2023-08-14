#install PyDictionary
#have a key/value pair that represents a word and its definition
#collect i/p from user, i/p is the word
#check if word is in dictionary
#print definition

from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes", "indentation", "head") #this is the import PyDictionary one
print(dictionary.getMeanings()) 

##the code below uses only 1 word at a time to display

# while True:
#     word = input("Enter the word you'd like to know the meaning of: ")
#     if word == "":
#         break
#     print(dictionary.meaning(word))

## the below code is for creating a dictionary and using it

# def main():
#     word_dictionary = {
#         'hi' : 'a way of greeting',
#         'eyes' : 'an organ for seeing',
#         'earth' : 'a planet in space'
#     }

#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         if word in word_dictionary:
            # print(word, ":", word_dictionary[word])
# main()