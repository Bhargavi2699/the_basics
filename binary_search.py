#function that takes list and target parameter
#multiple variables used: start, end, middle, steps
#recursion or while loop
#increase the steps each time a split is done.
#conditions to target position

def binary_search(list_elements, element):
    middle = 0
    start = 0
    end = len(list_elements)
    steps = 0

    while(start <= end):
        print("Step ", steps, ":", str(list_elements[start:end + 1]))

        steps += 1
        middle = (start + end) // 2

        if element == list_elements[middle]:
            return middle

        if element < list_elements[middle]:
            end = middle - 1
            #can use recursion and call binary_search() here and maybe see if you can get rid of the while loop
        else:
            start = middle + 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4

binary_search(my_list, target)