#game is basicaaly where there are blanks in a paragraph
#we will be using string concatenation - putting strings together
#For example : youtuber = " " --> some string variable
#a few ways to concatenate - using '+' or by using {}, with format(variable), f string - along with {variable_name}

#\ - is used to signify that the line has ended and it will continue to the next line

# youtuber = "Bugsy"
# print("Subscribe to " + youtuber) - +
# print("Subscribe to {}".format(youtuber)) - format()
# print(f"Subscribe to {youtuber}") - f string, cleanest way for concatenation

adj = input("Adjective: ")
verb1 = input("First verb: ")
verb2 = input("Second verb: ")
famous_person = input("Famous person: ")

madlibs = f"Computer programing is so {adj}! It makes so excited all the time because I love to {verb1}. Stay \
hydrated and {verb2} like you are {famous_person}!"

print(madlibs)
