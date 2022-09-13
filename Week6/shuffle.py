from random import randint
import time

def shuffle(nlist):
    length = len(nlist) # Get length of list

    for i in range(length): # Iterate through with range of length of list
        random_index = randint(i, length - 1) # Generate random index in range of list
        nlist[i], nlist[random_index] = nlist[random_index], nlist[i] # Swaps current index and random index generated
    return nlist # returns newly shuffled list


nlist = [7, 12, 18, 20, 25, 31, 36, 50, 88, 90, 100, 108]
print("Original list: ", nlist)

start_time = time.time()

shuffled_list = shuffle(nlist)
print("Shuffled List: ", shuffled_list)

end_time = time.time()

actual_time = (end_time - start_time)

print("Time Completed: ", actual_time)

# I think the time complexity of this algorithm is O(1) since we are iterating through the length of the list, 
# creating a random index, taking the current index and random index, swapping them around, and this process only completes once. 

# I would like to know how to modify this to be able to run multiple times and yield different results instead of a constant. Why is it doing that? 