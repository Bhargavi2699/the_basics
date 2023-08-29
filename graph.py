#this is our markov chain representation
#basically we connect a single word/node/vertex to another one which is the immediate word after a sentence to create a graph

import random

#defining the graph in terms of vertices
class Vertex:
    def __init__(self, value): #value will represent a word of the text
        self.value = value 
        #this 'adjacent dictionary will have a track of which nodes/vertices are connected to this vertex, 
        #these will be the keys the value will be the weight  
        self.adjacent = {} 
        #to keep track of neighbours & their weights
        self.neighbours = []
        self.neighbours_weights = []

    def add_edge_to(self, vertex, weight = 0): #we can add weight later but better to set it at 0       
        #this basically adds an edge to the vertex we i/p w/ weight
        self.adjacent[vertex] = weight #vertex in dictionary, value = weight
      
    def increment_edge(self, vertex):
        #this is incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1 #checks if we can get the value, else 0

    #map each word to it's probability, but put them in sep. lists
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbours_weights.append(weight)

    def next_word(self):
        #randomly select next word based on weights
        return random.choices(self.neighbours, weights = self.neighbours_weights)[0] #we still have to get back 1st item, hence 0
    
#we have our vertex rep., now we can put it in a graph
class Graph:
    def __init__(self):
        #initialize it to an empty dictionary, so a new word can be seen in it and get vertext object if present in dict.
        self.vertices = {}

    def get_vertex_values(self):
        #what values vertices have, aka, return all possible words
        return set(self.vertices.keys())
    
    #when we encounter a new word, we add a new vertex, we pass it a value which is the word it reps.
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    #putting the string to vertext mapping, we usually have the word, we just want to get the obj. it reps.
    def get_vertex(self, value): 
        #what if value isn't in the graph
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value] #get the object
    
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    #probability mappings of every single vertex
    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()

    

        
