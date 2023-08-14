#a dictionary that stores questions and answers
#have a variable that tracks the score of the player
#loop through the dictionary using the key-value pair
#display each question to the user and allow them to answer
#tell them if they're right or wrong
#show the result when the quiz is complete
#value for this case is gonna be another dictionary here

quiz = {
    "question1" : {
        "question" : "What is the capital of France?",
        "answer" : "Paris"
    },

    "question2" : {
        "question" : "What is the capital of Germany?",
        "answer" : "Berlin"
    },

    "question3" : {
        "question" : "What is the capital of Italy?",
        "answer" : "Rome"
    },

    "question4" : {
        "question" : "What is the capital of Spain?",
        "answer" : "Madrid"
    },

    "question5" : {
        "question" : "What is the capital of Portugal?",
        "answer" : "Lisbon"
    },

    "question6" : {
        "question" : "What is the capital of Switzerland?",
        "answer" : "Bern"
    },

    "question7" : {
        "question" : "What is the capital of Austria?",
        "answer" : "Vienna"
    }
}

score = 0

#looping through a dictionary
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score += 1
        print("Your score is: " + str(score))
        print()

    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("You score is: " + str(score))
        print()

print("You got " + str(score) + " out of 7 questions correctly.")
print("You got " + str(int(score / 7 * 100)) + "%")