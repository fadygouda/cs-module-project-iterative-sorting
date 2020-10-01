def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
            
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    min = 0
    max = len(arr) -1
    middle = 0
    while min <= max:
        middle = (min + max) // 2
        if arr[middle] < target:
            min = middle +1
        elif arr[middle] > target:
            max = middle -1
        else:
            return middle


    return -1  # not found
