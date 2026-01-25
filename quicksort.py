# quicksort selects a pivot (first element in this case)
# creates seperate arrays for values less and greater than pivot
# calls quicksort recursively on two sub arrays
# time complexity: O(nlogn)


def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
