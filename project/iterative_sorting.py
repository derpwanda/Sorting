# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through elements except the final element
    # it should be in the correct place since the previous elements
    # went through loop
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # temp = arr[smallest_index]
        # arr[smallest_index] = arr[cur_index]
        # arr[cur_index] = temp

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# try it out
print("Selection Sort")
my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(my_arr)
arr = selection_sort(my_arr)
print(my_arr)


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    # separate the first element from the rest of the array
    # current unsorted index

    # for all other indices, beginning with [1]:
    for index in range(1, len(arr)):

        # copy the item at that index into a temp variable
        cur_index = arr[index]
        prev_index = index - 1

        # iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        while prev_index >= 0:
            if cur_index < arr[prev_index]:

                # shift item over to the right as you iterate
                arr[prev_index + 1] = arr[prev_index]

                # when the correct index is found, copy temp into this position
                arr[prev_index] = cur_index
                prev_index = prev_index - 1

            else:
                break

    return arr


# try it out
print("Insertion Sort")
arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(arr)
arr = insertion_sort(arr)
print(arr)


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) -1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # python swapping
    return arr

    # found online https://www.youtube.com/watch?v=UOuH8IVFAGk
    # while True:
    #     corrected = False
    #     for i in range(0, len(arr) - 1):
    #         if arr[i] > arr[i + 1]:
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #             corrected = True
    #     if not corrected:
    #         return arr

    # a lecture solution (doesn't pass test!)
    # is_sorted = False
    # while not is_sorted:
    #     is_sorted = True

    #     for i in range(len(arr) - 1):
    #         if arr[i] > arr[i + 1]:
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #             is_sorted = False
    #     return arr
    
#     def bubble_sort( arr ):
#     for i in range(0, len(arr) - 1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#         if i != 0 and arr[i] < arr[i-1]:
#             arr[i], arr[i-1] = arr[i-1], arr[i]

#     return arr


# try it out
print("Bubble Sort")
arr = ['b', 'd', 'a', 'f', 'c', 'e']
print(arr)
arr = bubble_sort(arr)
print(arr)

arr = [4, 2, 3, 1, 6, 5]
print(arr)
arr = bubble_sort(arr)
print(arr)

arr = [6, 5, 4, 3, 2, 1]
print(arr)
arr = bubble_sort(arr)
print(arr)


# STRETCH: implement the Count Sort function below
# count sort is useful for small ranges
# You count how many of each digit there is, and then you determine each digit's starting position by counting how many cells are taken up by the digits before it

#  In computer science, counting sort is an algorithm for sorting a collection 
# of objects according to keys that are small integers; that is, it is an
# integer sorting algorithm.

def count_sort(arr, maximum ):

    m = maximum + 1
    count = [0] * m

    for a in arr:
        # count occurences
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

print('countsort')
print(count_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))
