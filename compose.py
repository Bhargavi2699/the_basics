import os
import re
import string
import random
# from matplotlib import textpath
from graph import Graph, Vertex

def get_words_from_text(text_path):#pass the path from which we're getting the words from
    with open(text_path, 'r') as f:
        text = f.read()

        #remove [] and [text in there]
        #'.' - any character; '+' - more than one of them; \[ and \] - the brackets; it gets replaced with ' '
        text = re.sub(r'\[(.+)\]', ' ', text)

        #get's rid of all extra stuff and replaces with single space       
        text = ' '. join(text.split()) 
        #now we can be 'complex' and deal with punctuation... but there are cases where you might want to add a '.'
        #such as (Mr.Brightside), but its' not really punctuation...so we just remove them all
        #maketrans - make translation
        #hello! it's me. --> hello its me
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split() #split on spaces...again
    return words

def make_graph(words):
    g = Graph()

    previous_word = None #bcoz at the beginning, there is not previous word

    #for each word, check that the word is in the graph, 
    for word in words:
        #if there was a previous word, then add an edge to it if it does not already exist
        word_vertex = g.get_vertex(word)       
        #in the graph, increment the weiight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

        #set our word to previous word and then iterate
        previous_word = word_vertex
    #remember, we want to generate the probability mappings before composing, this is a gr8 place to do it, b4 we return graph object
    g.generate_probability_mappings()
    return g

def compose(g, words, length = 50): #everytime we generate a new word, we add it to this list comprehensiom
    composition = []
    word = g.get_vertex(random.choice(words)) #start by picking random word
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main(artist):
    #step 1: get words from text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    #for song lyrics
    words = []
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)
    #step 2: make a graph using those words
    g = make_graph(words)
    #step 3: get the next word for x number of words(defined by user)
    #step 4: show the results to user
    composition = compose(g, words, 100)
    return ' '.join(composition) #returns a string where all the words are seperated by a space.

if __name__ == "__main__":
    print(main('linkin_park'))