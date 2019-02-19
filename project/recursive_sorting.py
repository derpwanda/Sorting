### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
# a SORTED POSITION is when all the other elements on the left-hand side
# are smaller than the SORTED POSITION and the elements on the right-hand
# side are equal-to or greater than the SORTED POSITION.
def quick_sort( arr, low, high ):
    #for each UNSORTED POSITION
    #   set PIVOT arr[0] (the first value in the list)
    #   the low will be the pivot + 1
    #   the high is the arr[len - 1]

        # while loop?
        #   increment the low until we hit a value that is greater than the pivot
        #   STOP

        #   decrement the high until we hit a value that is less than the pivot
        #   STOP
        
        #   Flip these two values

        #   CONTINUE

        #   STOP when you hit the split point, when the low and high cross

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
