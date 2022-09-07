# Binary search is a strategy used to find elements within a list by consistenly reducing the amount of data to be searched.
# List must already be sorted.

def binary_search(list, term):
    start = 0 # First index
    last = len(list) - 1 # Last index

    while start <= last: # While number isn't found

        middle = start + (last - start) // 2 # Calculate middle point in list

        if list[middle] == term: # If middle of list is equal to term
            return True 
        elif list[middle] < term: # If middle of list is less than term, search left side of list, else, search right side of list.
            start = middle + 1
        else:
            last = middle - 1
    return False


        

my_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(binary_search(my_list, 31)) # Find 31
print(binary_search(my_list, 77)) # Find 77

my_list_2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]
print(binary_search(my_list_2, "Delta")) # Find "Delta"