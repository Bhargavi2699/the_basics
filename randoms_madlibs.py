from samples_madlibs import code, hp, hunger_games, zombies
import random

if __name__ == "__main__":
#regular list/sequences, where the madlib is chosen from one of these 4 files, since all of them have madlib() func.
    m = random.choice([code, hp, hunger_games, zombies]) 
    print(m)
    m.madlib()                                          