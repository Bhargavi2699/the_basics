#rock > scissors; scissors > paper; paper > rock

import random

def play():
    user = input("Choose between rock 'r', paper 'p' and scissors 's': ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a Tie!!'
    
    #here we check the below function, note: we are not calling it just checking the conditions
    #hence indentation is importatnt
    if is_win(user, computer):
        return "You win!!"
    
    #using only a return statement instead of an else statement, since the above 2 are already passed.
    #or you can do, if is_win(computer, user): where parameters are being flipped, and return "you lose"
    return "You lose."
    
def is_win(player, opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())  #can perfrm function calls like this as well
