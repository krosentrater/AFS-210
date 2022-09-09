def mergeSort(nlist):
    print("Splitting ",nlist)
    if (len(nlist) <= 1): # If length of list less than or equal to 1
        return nlist
    half = len(nlist) // 2 # Find half of list
    left = mergeSort(nlist[:half]) # recursively call left half
    right = mergeSort(nlist[half:]) # recursively call right half
    return merge(nlist, left, right) # Base case met, return INTO merge function


def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    print("Merging ",nlist)
    return nlist

my_list = [55, 31, 26, 20, 63, 7, 51, 74, 81, 40]
mergeSort(my_list)