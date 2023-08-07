print("Welcome to my computer quiz!!!")

playing = input("Do you want to play the game? ")
#print(playing)

#lower()(inbuilt func btw) is used here to convert all of our answers to a particular consistent way
# #hence both 'playing' and 'answer' has .lower() in it.
if playing.lower() != "yes": #True or False, checking Boolean
    quit() #terminates your program - inbuilt function

print("Awesome! Let's play!:P") #if yes, print this stmt

score = 0 

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!Cool!!') #can use ' ' or " " interchageably, just make sure you remember to be consistent
    score += 1
else:
    print('Incorrect!Boo!!')

#can use the variable repeatedly, as it's usage is already up after 'if' stmt
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!Cool!!') 
    score += 1
else:
    print('Incorrect!Boo!!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!Cool!!') 
    score += 1
else:
    print('Incorrect!Boo!!')

#can do .lower() in the i/p as well, but not in variable dec, as syntax error occurs.
answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print('Correct!Cool!!')
    score += 1
else:
    print('Incorrect!Boo!!')

#str() type conversion/casting is done because concatenation of diff datatypes is not possible
print("Your final score is " + str(score))
#getting percentage - BODMAS/PEMDAS lol
print("Your final percentage is " + str(score / 4 * 100) +"%")