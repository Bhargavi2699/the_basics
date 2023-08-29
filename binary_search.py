import random
import time

#implementing binary search algorithm, also to prove binary is faster than naive(linear) search algorithm
#linear/naive search : scans the entire list and finds the element, if present, return element, else return -1

#start by defining naive search
def naive_search(l, target):
    #example l = [1, 3, 10, 34]
    for i in range(len(l)):
        if l[i] == target:
            return target
        else:
            return -1
        
#binary search uses divide and conquer, using the fact that our list is sorted
def binary_search(l, target, low = None, high = None):
    #example l = [1, 3, 5, 10, 34]
    if low is None:
        low = 0

    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2 #rounds off the final value into an integer

    if l[midpoint] == target: 
        return target
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1) #using recursion by calling the function to itself
    else:
        #target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high) #using recursion by calling the function to itself
    
if __name__ == "__main__":
    # l = [1, 3, 5, 10, 25]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    #build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length: 
        sorted_list.add(random.randint(-3 * length, 3 * length)) #range is -30000 to 30000
    sorted_list = sorted(list(sorted_list)) #making it completely sorted now

    #so right now we're making everything the target in the list
    start = time.time() #checking the time stamp ....and stuff
    for target in sorted_list:
        naive_search(sorted_list, target) #naive_search is run 10000 times here
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time() #checking the time stamp ....and stuff
    for target in sorted_list:
        binary_search(sorted_list, target) #naive_search is run 10000 times here
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")



        


